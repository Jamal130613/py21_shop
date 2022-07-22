from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.product.views import CategoryView, ProductView, CommentView
from applications.product.views import CategoryView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('', ProductView)
router.register('comment/', CommentView)

urlpatterns = [
    # path('category/', CategoryView.as_view({'get': 'list'})),
    path('', include(router.urls))
]
# TODO:Реализовать работы с комментарием и переопределить to representation  на вывод комментариев к продукту
