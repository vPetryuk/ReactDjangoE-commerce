from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    re_path('api-auth/', include('rest_framework.urls')),
    re_path('rest-auth/', include('rest_auth.urls')),
    re_path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('admin/', admin.site.urls),
    re_path('api/', include('core.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += [re_path(r'^.*',
                            TemplateView.as_view(template_name='index.html'))]
