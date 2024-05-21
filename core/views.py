import os

import pandas as pd
from django.shortcuts import render
from django.views import View

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
