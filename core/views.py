import os

import pandas as pd
from django.shortcuts import render
from django.views import View

from .tools.matplotlib_graphs import get_graphs
from .tools.stats import get_table


class MyView(View):
    @staticmethod
    def get(request):
        return render(request, "core/base.html")

    @staticmethod
    def post(request):
        uploaded_file = request.FILES["filename"]
        # fs = FileSystemStorage()
        # filename = fs.save(uploaded_file.name, uploaded_file)
        # file_url = fs.url(filename)
        # context = {"file_url": file_url}
        # return render(request, "core/index.html", context)

        df = pd.read_csv(uploaded_file)
        table = get_table(df)
        graphs = get_graphs(df)
        graphs_list = [os.path.join(graphs, f) for f in os.listdir(graphs) if f.endswith(".png")]
        columns = table.columns.tolist()
        table = table.values.tolist()
        context = {"table": table, "columns": columns, "graphs_list": graphs_list}
        return render(request, "core/index.html", context)
