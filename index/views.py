from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index/index.html'


class AboutView(TemplateView):
    template_name = 'index/about.html'


class ContactView(TemplateView):
    template_name = 'index/contact.html'


class BrandDesignService(TemplateView):
    template_name = 'index/brand-design.html'


class CampaignDesignService(TemplateView):
    template_name = 'index/campaign-design.html'


class VisualIdentityService(TemplateView):
    template_name = 'index/visual-identity.html'


class PhotographyAndVideographyService(TemplateView):
    template_name = 'index/video-photography.html'


class ContentCreationService(TemplateView):
    template_name = 'index/content-creation-service.html'


class PortfolioDetailSample(TemplateView):
    template_name = 'index/portfolio-detail.html'


class PortfolioVianaDetail(TemplateView):
    template_name = 'index/portifolio-viana.html'


class PortfolioZelmondDetail(TemplateView):
    template_name = 'index/portfolio-zelmond.html'

class PortfolioLucanoDetail(TemplateView):
    template_name = 'index/portfolio-lucano.html'


class PortfolioNavarDetail(TemplateView):
    template_name = 'index/portfolio-navar.html'


class PortfolioNetentPokerDetail(TemplateView):
    template_name = 'index/portfolio-netentpoker.html'


class PortfolioBreakingMuscleDetail(TemplateView):
    template_name = 'index/portfolio-breakingmuscle.html'


class PortfolioDyarinoDetail(TemplateView):
    template_name = 'index/portfolio-dyarino.html'


class PortfolioSBTDetail(TemplateView):
    template_name = 'index/portfolio-sbt.html'


class PortfolioTalashimDetail(TemplateView):
    template_name = 'index/portfolio-talashim.html'


class PortfolioKunziteDetail(TemplateView):
    template_name = 'index/portfolio-kunzite.html'


class PortfolioRegenbogenDetail(TemplateView):
    template_name = 'index/portfolio-regenbogen.html'


class PortfolioNegahDetail(TemplateView):
    template_name = 'index/portfolio-negah.html'


class PortfolioNegahbanmamutDetail(TemplateView):
    template_name = 'index/portfolio-negahban-mammut.html'


class PortfolioBunnyModeDetail(TemplateView):
    template_name = 'index/portfolio-bunny-mode.html'


class PortfolioAzkiDetail(TemplateView):
    template_name = 'index/portfolio-azki.html'


class PortfolioMonjiDetail(TemplateView):
    template_name = 'index/portfolio-monji.html'


class PortfolioKanirushDetail(TemplateView):
    template_name = 'index/portfolio-kanirush.html'


class PortfolioCheraghBarghDetail(TemplateView):
    template_name = 'index/portfolio-cheraghbargh.html'


class PortfolioMammutVIPTourDetail(TemplateView):
    template_name = 'index/portfolio-mammut-vip-tour.html'


class PortfolioView(TemplateView):
    template_name = 'index/portfolio.html'


class PortfolioVitaView(TemplateView):
    template_name = 'index/portfolio-vita.html'


class PortfolioVestaView(TemplateView):
    template_name = 'index/portfolio-vesta.html'


class PortfolioHapitooView(TemplateView):
    template_name = 'index/portfolio-hapitoo.html'


class PortfolioSamView(TemplateView):
    template_name = 'index/portfolio-sam.html'


class WorksView(TemplateView):
    template_name = 'index/works.html'