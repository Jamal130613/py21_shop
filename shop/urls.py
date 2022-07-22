from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Python 21 shop',
        default_version='v1',
        description='Наш первый интернет магазин'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/product/', include('applications.product.urls')),
    path('api/v1/order/', include('applications.cart.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
