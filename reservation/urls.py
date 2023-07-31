from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet) #Automaically generates URL patterns for all actions supported by BookingViewSet (listing bookings, creating bookings, retrieve single, update , delete)

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.home, name = 'home'),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),

]
    
