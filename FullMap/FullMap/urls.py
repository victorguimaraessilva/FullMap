from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from map import views
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    ### Index
    url(r'^', views.index,),
    
]
urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)