import os
import shutil
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from django_csv_analysis import settings

from .forms import LoginForm, RegisterForm
from .models import UploadRecord
from .tools.matplotlib_graphs import get_graphs
from .tools.stats import get_table
from .tools.ydata_stats import get_html


class MyView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "core/base.html")

    @staticmethod
    def post(request: HttpRequest) -> Any:
        uploaded_file = request.FILES.get("filename")
        if not uploaded_file:
            return render(request, "core/base.html", {"error_message": "File upload failed."})

        uploaded_df = pd.read_csv(uploaded_file)

        table = get_table(uploaded_df)
        columns = table.columns.tolist()
        table = table.to_numpy().tolist()

        graphs = get_graphs(uploaded_df)
        graphs_list = [os.path.join(graphs, f) for f in os.listdir(graphs) if f.endswith(".png")]

        # Сохраняем DataFrame в сессии для последующего использования
        request.session["df"] = uploaded_df.to_json()

        # Проверяем, аутентифицирован ли пользователь и создаем запись в базе данных без заполнения file_address
        if request.user.is_authenticated:
            upload_record = UploadRecord.objects.create(
                user=request.user,
                filename=uploaded_file.name,
                folder_address=graphs,
            )
            # Сохраняем ID записи в сессии для последующего обновления
            request.session["upload_record_id"] = upload_record.id

        context = {"table": table, "columns": columns, "graphs_list": graphs_list}
        return render(request, "core/index.html", context)

    @staticmethod
    def generate_ydata_html(request: HttpRequest) -> JsonResponse:
        df_json = request.session.get("df")
        if df_json is None:
            return JsonResponse({"error": "No data found"}, status=404)

        uploaded_df = pd.read_json(df_json)
        ydata_html_path = get_html(uploaded_df)
        relative_path = os.path.relpath(ydata_html_path, settings.MEDIA_ROOT)
        report_url = f"/media/{relative_path}"

        # Обновляем запись в базе данных
        upload_record_id = request.session.get("upload_record_id")
        if request.user.is_authenticated and upload_record_id:
            upload_record = UploadRecord.objects.get(id=upload_record_id)
            upload_record.file_address = relative_path
            upload_record.save()

        return JsonResponse({"report_url": report_url})


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy("login")


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "core/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return redirect("home")


class History(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return render(request, "core/login.html", {"error_message": "Please log in to view your history."})
        upload_records = UploadRecord.objects.filter(user=request.user)

        # Передаем записи в шаблон для отображения
        context = {"upload_records": upload_records}
        return render(request, "core/history.html", context)


class DownloadArchiveView(View):
    def get(self, request: HttpRequest, record_id: int) -> HttpResponse:
        record = UploadRecord.objects.get(id=record_id, user=request.user)

        folder_path = record.folder_address
        if not Path.exists(folder_path):
            msg = "Folder does not exist"
            raise Http404(msg)

        # Создаем временный файл для архива
        temp_archive = tempfile.NamedTemporaryFile(delete=False)
        shutil.make_archive(temp_archive.name, "zip", folder_path)
        temp_archive.close()

        # Отправляем архив пользователю
        response = HttpResponse(open(temp_archive.name + ".zip", "rb").read(), content_type="application/zip")
        response["Content-Disposition"] = f'attachment; filename="{record.filename}.zip"'

        # Удаляем временный архивный файл
        os.remove(temp_archive.name + ".zip")

        return response
