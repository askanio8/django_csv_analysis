import os

import pandas as pd
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm, LoginForm
from .tools.matplotlib_graphs import get_graphs
from .tools.stats import get_table
from .tools.ydata_stats import get_html


class MyView(View):
    @staticmethod
    def get(request):
        return render(request, "core/base.html")

    @staticmethod
    def post(request):
        uploaded_file = request.FILES["filename"]
        df = pd.read_csv(uploaded_file)

        table = get_table(df)
        columns = table.columns.tolist()
        table = table.values.tolist()

        graphs = get_graphs(df)
        graphs_list = [os.path.join(graphs, f) for f in os.listdir(graphs) if f.endswith(".png")]

        ydata_html = get_html(df)
        context = {"table": table, "columns": columns, "graphs_list": graphs_list, "ydata_html": ydata_html}
        return render(request, "core/index.html", context)


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "core/login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')