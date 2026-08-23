from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', include('core.urls')),
    path('', RedirectView.as_view(pattern_name='room_list')),
]