from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/logo-design', LogoArchive.as_view(), name='logo-design-archive'),
    path('portfolio/visual-brand-identity', DigitalArchive.as_view(), name='digital-branding'),
    path('portfolio/motion-design', MotionDesignArchive.as_view(), name='motion-design'),
    path('portfolio/advertising-photography', AdvertisingPhotoArchive.as_view(), name='advertising-photography'),
    path('portfolio/illustration', IllustrationArchive.as_view(), name='illustration'),
    path('portfolio/gamification', GameDesignArchive.as_view(), name='gamification'),
    path('portfolio/video-making', VideoMakingArchive.as_view(), name='video-making'),
    path('portfolio/detail', PortfolioDetailSample.as_view(), name='portfolio-detail'),
]