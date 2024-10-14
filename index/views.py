from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index/index.html'


class AboutView(TemplateView):
    template_name = 'index/about.html'


class ContactView(TemplateView):
    template_name = 'index/contact.html'


class PortfolioListView(TemplateView):
    template_name = 'index/portfolio-list.html'


class PortfolioDetailSample(TemplateView):
    template_name = 'index/portfolio-detail.html'

