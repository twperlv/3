"""
URL configuration for response_types project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example_4.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("simple/", simple_http_response),
    path("redirect/", redirect_response),
    path("permanent_redirect/", permanent_redirect_response),
    path("not_modified/", not_modified_response),
    path("bad_request/", bad_request_response),
    path("forbidden/", forbidden_response),
    path("gone/", gone_response),
    path("server_error/", server_error_response),
    path("not_found/", not_found_response),
    path("json/", json_response),
    path("stream/", stream_response),
    path("file/", file_response)
]
