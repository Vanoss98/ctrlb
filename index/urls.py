from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolio/detail', PortfolioDetailSample.as_view(), name='portfolio-detail'),
]