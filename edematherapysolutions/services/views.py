from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.views import CommonPageView


class ServicesView(CommonPageView):
    page_name = 'services'
    def get_context_data(self, **kwargs):
        print("here")
        return {}
