from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),

    path('portfolio/brand-design', BrandDesignService.as_view(), name='brand-design'),
    path('portfolio/campaign-design', CampaignDesignService.as_view(), name='campaign-design'),
    path('portfolio/photgraphy-and-videography', PhotographyAndVideographyService.as_view(), name='photgraphy-and-videography'),
    path('portfolio/visual-identity', VisualIdentityService.as_view(), name='visual-identity'),
    path('portfolio/content-creation', ContentCreationService.as_view(), name='content-creation'),


    path('portfolio/detail', PortfolioDetailSample.as_view(), name='portfolio-detail'),
    path('portfolio/viana/detail', PortfolioVianaDetail.as_view(), name='portfolio-viana'),
    path('portfolio/zelmond/detail', PortfolioZelmondDetail.as_view(), name='portfolio-zelmond'),
    path('portfolio/lucano/detail', PortfolioLucanoDetail.as_view(), name='portfolio-lucano'),
    path('portfolio/navar/detail', PortfolioNavarDetail.as_view(), name='portfolio-navar'),
    path('portfolio/netent-poker/detail', PortfolioNetentPokerDetail.as_view(), name='portfolio-netentpoker'),
    path('portfolio/breaking-muscle/detail', PortfolioBreakingMuscleDetail.as_view(), name='portfolio-breaking-muscle'),
    path('portfolio/dyarino/detail', PortfolioDyarinoDetail.as_view(), name='portfolio-dyarino'),
    path('portfolio/sbt/detail', PortfolioSBTDetail.as_view(), name='portfolio-sbt'),
    path('portfolio/talashim/detail', PortfolioTalashimDetail.as_view(), name='portfolio-talashim'),
    path('portfolio/kunzite/detail', PortfolioKunziteDetail.as_view(), name='portfolio-kunzite'),
    path('portfolio/regenbogen/detail', PortfolioRegenbogenDetail.as_view(), name='portfolio-regenbogen'),
    path('portfolio/negah-holding/detail', PortfolioNegahDetail.as_view(), name='portfolio-negah'),
    path('portfolio/negahban-mammut/detail', PortfolioNegahbanmamutDetail.as_view(), name='portfolio-negahban-mammut'),
    path('portfolio/avakatan/detail', PortfolioBunnyModeDetail.as_view(), name='portfolio-bunny-mode'),
    path('portfolio/azki/detail', PortfolioAzkiDetail.as_view(), name='portfolio-azki'),
    path('portfolio/monji/detail', PortfolioMonjiDetail.as_view(), name='portfolio-monji'),
    path('portfolio/kanirush/detail', PortfolioKanirushDetail.as_view(), name='portfolio-kanirush'),
    path('portfolio/cheragh-bargh/detail', PortfolioCheraghBarghDetail.as_view(), name='portfolio-cheraghbargh'),
    path('portfolio/mammut-vip-tour/detail', PortfolioMammutVIPTourDetail.as_view(), name='portfolio-mammut-vip-tour'),
    path('portfolio/vita/detail', PortfolioVitaView.as_view(), name='portfolio-vita'),
    path('portfolio/vesta/detail', PortfolioVestaView.as_view(), name='portfolio-vesta'),
    path('portfolio/hapitoo/detail', PortfolioHapitooView.as_view(), name='portfolio-hapitoo'),
    path('portfolio/sam/detail', PortfolioSamView.as_view(), name='portfolio-sam'),

    path('works/', WorksView.as_view(), name='works'),
]