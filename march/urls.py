
from django.conf.urls.static import static
from march import settings

from django.contrib import admin
from django.urls import path, include
from .views import (
    home, sidebar_partial,

)

urlpatterns = [

    path('sidebar', sidebar_partial, name='sidebar'),


    path('', home),
    path('', include( 'ACCOUNTS.urls'       )),
    path('', include( 'marchPRODUCTS.urls'  )),
    path('', include( 'marchCATEGORIES.urls')),
    path('', include( 'marchCart.urls'      )),
    path('', include( 'marchSITEINFO.urls'  )),
    path('', include( 'marchCOMMENTS.urls'  )),





    path('admin/', admin.site.urls),

    
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
