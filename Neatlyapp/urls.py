from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('daf/', views.Daf, name='daf'),
    path('iveco/', views.Iveco, name='iveco'),
    path('man/', views.Man, name='man'),
    path('mecerdes/', views.Mercerdes, name='mercedes'),
    path('renalt/', views.Renault, name='renault'),
    path('scania/', views.Scania, name='scania'),
    path('volvo/', views.Volvo, name='volvo'),
    path('custom/', views.Custom, name='custom'),
    path('heavyduties/', views.HeavyDuties, name='heavy duties'),
    path('contact/', views.contact_view, name='contact_view'),
    path('thank-you/', views.thank_you, name='thank_you'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)