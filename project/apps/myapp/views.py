import json

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.http import JsonResponse

from project.apps.myapp.forms import PersonForm
from project.apps.myapp.models import Person

# Create your views here.
class Index(TemplateView):
    http_method_names = ['get']
    template_name = 'myapp/index.html'


class Create(CreateView):
    http_method_names = ['get', 'post']
    form_class = PersonForm
    template_name = 'myapp/create.html'

    def post(self, request, *args, **kwargs):
        data = None
        status = None
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            data = {'success': True}
            status = 201
        else:
            data = json.dumps(dict(form.errors.items()), ensure_ascii=False)
            status = 400
        return JsonResponse(data, safe=False, status=status)


class List(ListView):
    http_method_names = ['get']
    model = Person
    template_name = 'myapp/list.html'


class Detail(UpdateView):
    http_method_names = ['get', 'post']
    form_class = PersonForm
    pk_url_kwarg = 'id'
    template_name = 'myapp/detail.html'

    def post(self, request, *args, **kwargs):
        data = None
        status = None
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            data = {'success': True}
            status = 200
        else:
            data = json.dumps(dict(form.errors.items()), ensure_ascii=False)
            status = 400
        return JsonResponse(data, safe=False, status=status)