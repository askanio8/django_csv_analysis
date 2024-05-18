from django.shortcuts import render

from .tools.statistics import get_table


def index(request):
    table = get_table("...")
    columns = table.columns.tolist()
    table = table.values.tolist()
    context = {"table": table, "columns": columns}
    return render(request, "core/index.html", context)
