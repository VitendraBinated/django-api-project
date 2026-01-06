from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    external_posts,
    product_summary_report
)

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('external-posts/', external_posts),
    path('report/summary/', product_summary_report),
]
