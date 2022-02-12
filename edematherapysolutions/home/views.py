from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.template import TemplateDoesNotExist

class CommonPageView(View):
    def get_app_name(self):
        return self.__module__.split('.')[0]
    app_name = property(get_app_name)

    def get_context_data(self, **kwargs):
        return {}

    def get_template_name(self, pageName):
        return f'{self.app_name}/{pageName.lower()}.jinja'

    def get_template_filename(self, template_name):
        print('APP', self.app_name)
        print('temp', template_name)
        return f'{self.app_name}/templates/{template_name}'

    def get(self, request, pageName=None, **kwargs):
        if not pageName:
            pageName = self.page_name
        kwargs['pageName'] = pageName
        template_name = self.get_template_name(pageName)
        template_filename = self.get_template_filename(template_name)
        context = self.get_context_data(request=request, **kwargs)

        try:
            return render(request, template_name, context)
        except TemplateDoesNotExist:
            raise Http404(f'File does not exist: {template_filename}')


class Home(CommonPageView):
    page_name = 'base'
    def get_context_data(self, **kwargs):
        print('here')
        return {}
