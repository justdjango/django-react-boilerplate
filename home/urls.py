from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
import os


# The precache-manifest may be generated with a new name, so we need to get it manually
files_in_root = []
for file in os.listdir(os.path.join(settings.BASE_DIR, 'build')):
    files_in_root.append(file)
precache_manifest_path = [f for f in files_in_root if ("precache-manifest" in f)][0]

urlpatterns = [
    path('asset-manifest.json', (TemplateView.as_view(template_name="asset-manifest.json",
                                                      content_type='application/manifest+json', )),
         name='asset-manifest.json'),
    path('service-worker.js', (TemplateView.as_view(template_name="service-worker.js",
                                                    content_type='application/javascript', )),
         name='service-worker.js'),
    path(precache_manifest_path, (
        TemplateView.as_view(template_name=precache_manifest_path,
                             content_type='application/javascript', )),
         name=precache_manifest_path),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
