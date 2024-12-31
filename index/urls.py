from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/visual-identity-and-graphic-design', LogoArchive.as_view(), name='logo-design-archive'),
    path('portfolio/business-and-brand-identity', DigitalArchive.as_view(), name='digital-branding'),
    path('portfolio/motion-design', MotionDesignArchive.as_view(), name='motion-design'),
    path('portfolio/photgraphy-and-videography', AdvertisingPhotoArchive.as_view(), name='photgraphy-and-videography'),
    path('portfolio/campaign', IllustrationArchive.as_view(), name='campaign'),
    path('portfolio/gamification', GameDesignArchive.as_view(), name='gamification'),
    path('portfolio/video-making', VideoMakingArchive.as_view(), name='video-making'),
    path('portfolio/detail', PortfolioDetailSample.as_view(), name='portfolio-detail'),
    path('portfolio/viana/detail', PortfolioVianaDetail.as_view(), name='portfolio-viana'),
    path('portfolio/zelmond/detail', PortfolioZelmondDetail.as_view(), name='portfolio-zelmond'),
    path('portfolio/lucano/detail', PortfolioLucanoDetail.as_view(), name='portfolio-lucano'),
]