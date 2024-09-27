# urls.py (project-level)
from django.contrib import admin
from django.urls import path, include
from Authentications import urls as authurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(authurls)),
    # path('products/', include(urls)),  # Include Product app URLs with namespace and app_name
]
