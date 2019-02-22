from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path(
        '',
        include('loan.urls')
    ),
    path('api/', include('api.urls')),
    # re_path('api/(?P<version>(v1|v2))/', include('api.urls'))

]
