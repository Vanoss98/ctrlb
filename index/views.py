from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index/index.html'


class AboutView(TemplateView):
    template_name = 'index/about.html'


class ContactView(TemplateView):
    template_name = 'index/contact.html'


class LogoArchive(TemplateView):
    template_name = 'index/logo-archive.html'


class DigitalArchive(TemplateView):
    template_name = 'index/digital-branding-archive.html'


class MotionDesignArchive(TemplateView):
    template_name = 'index/motion-design-archive.html'


class AdvertisingPhotoArchive(TemplateView):
    template_name = 'index/ad-photo-archive.html'


class IllustrationArchive(TemplateView):
    template_name = 'index/illustration-archive.html'


class GameDesignArchive(TemplateView):
    template_name = 'index/game-design-archive.html'


class VideoMakingArchive(TemplateView):
    template_name = 'index/video-making-archive.html'


class PortfolioDetailSample(TemplateView):
    template_name = 'index/portfolio-detail.html'
