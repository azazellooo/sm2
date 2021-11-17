from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, UpdateView

from .models import Content
from .forms import ContentForm


class ContentListView(ListView, FormMixin):
    model = Content
    context_object_name = 'contents'
    template_name = 'content/index.html'
    form_class = ContentForm
    ordering = '-created_at'
    paginate_by = 500
    paginate_orphans = 10

    def get_queryset(self):
        return Content.objects.using('metrics').all()[:10]


def create_content(request, *args, **kwargs):
    if request.is_ajax and request.method == "POST":
        data = request.POST
        content = Content.objects.using('metrics').create(
            project_name=data.get("project_name"),
            name_content=data.get('name_content'),
            resource=data.get('resource'),
            id_format_content=data.get('id_format_content'),
            url=data.get('url'),
            success=data.get('success'),
            success_data_update=data.get('success_data_update'),
            acc_type=data.get('acc_type')
        )
        return JsonResponse({'message': f'content "{content.name_content}" is created successfully'}, status=200)
    return JsonResponse({"error": "something went wrong..."}, status=400, safe=False)


def delete_content(request, *args, **kwargs):
    if request.is_ajax and request.method == 'POST':
        content = Content.objects.using('metrics').get(content_id=list(dict(request.POST).keys())[0])
        content.delete()
        return JsonResponse({'message': f'content "{content.name_content}" is deleted successfully'}, status=200)
    return JsonResponse({"error": "something went wrong..."}, status=400, safe=False)


class ContentUpdateView(UpdateView):
    model = Content
    form_class = ContentForm

    def get(self, request, *args, **kwargs):
        content = Content.objects.using('metrics').get(content_id=kwargs.get('pk'))
        form = ContentForm(instance=content)
        return HttpResponse(form.as_p())

    def post(self, request, *args, **kwargs):
        data = request.POST
        if request.is_ajax:
            content = Content.objects.using('metrics').get(content_id=kwargs.get('pk'))
            content.project_name = data.get("project_name")
            content.name_content = data.get('name_content')
            content.resource = data.get('resource')
            content.id_format_content = int(data.get('id_format_content')[0])
            content.url = data.get('url')
            content.success = int(data.get('success')[0])
            content.success_data_update = int(data.get('success_data_update')[0])
            content.acc_type = int(data.get('acc_type')[0])
            content.save()
            return JsonResponse({'message': f'content "{content.name_content}" is updated successfully'})
        return JsonResponse({"error": "something went wrong..."}, status=400, safe=False)