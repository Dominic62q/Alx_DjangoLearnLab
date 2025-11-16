from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('your_app.can_view', raise_exception=True)
def article_list(request):
    return render(request, "articles/list.html")


@permission_required('your_app.can_create', raise_exception=True)
def article_create(request):
    return render(request, "articles/create.html")


@permission_required('your_app.can_edit', raise_exception=True)
def article_edit(request, pk):
    return render(request, "articles/edit.html")


@permission_required('your_app.can_delete', raise_exception=True)
def article_delete(request, pk):
    return render(request, "articles/delete.html")
