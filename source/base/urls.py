from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.account.api.v1.urls', namespace='account.v1')),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# This is only needed when using runserver.(debug is true)
if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view
    from rest_framework.permissions import AllowAny

    schema_view = get_schema_view(
        openapi.Info(
            title='Ecommerce Backend APIS',  # f'{settings.SITE["NAME"]} APIs'
            # f'{settings.REST_FRAMEWORK["DEFAULT_VERSION"]}'
            default_version='V1',
            # f'{settings.SITE["DESCRIPTION"]}'
            description='This is documentation for the backend API',
            # f'{settings.DEFAULT_FROM_EMAIL}'
            contact=openapi.Contact(email='arezoo@gmail.com')
        ),
        public=True,
        permission_classes=(AllowAny,)
    )
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui')
    ]
