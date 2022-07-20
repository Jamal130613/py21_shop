from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.product.views import CategoryView, ProductView
from applications.product.views import CategoryView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('', ProductView)

urlpatterns = [
    # path('category/', CategoryView.as_view({'get': 'list'})),
    path('', include(router.urls))
]
