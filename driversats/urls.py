
from django.contrib import admin
from django.urls import path, include

from aaaStats.views import home_view

urlpatterns = [
    path('', home_view, name='aaaSats'),
    path('admin/', admin.site.urls),
]
