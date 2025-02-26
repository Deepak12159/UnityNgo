# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
# ]

from django.urls import path
from .views import admin_dashboard, orphan_list, orphan_create, orphan_update, orphan_delete

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    # Orphan Kids URLs
    path('orphans/', orphan_list, name='orphan_list'),
    path('orphans/new/', orphan_create, name='orphan_create'),
    path('orphans/edit/<int:id>/', orphan_update, name='orphan_update'),
    path('orphans/delete/<int:id>/', orphan_delete, name='orphan_delete'),
]
