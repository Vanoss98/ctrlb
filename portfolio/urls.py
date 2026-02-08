from django.urls import path
from .views import *


urlpatterns = [
    path('portfolio/jeanwest/', PortfolioJeanwest.as_view(), name='jeanwest'),
]
