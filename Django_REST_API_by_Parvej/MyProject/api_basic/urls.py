from django.urls import path, include
from .views import article_list, article_detail, article_list_apiview, article_detail_apiview, ArticleAPIView, \
    ArticleDetailsAPIView, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('articles', ArticleGenericViewSet, basename='article')
router.register('articlesmodel', ArticleModelViewSet, basename='article')

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:id>/', article_detail),
    path('article_apiview/', article_list_apiview),
    path('detail_apiview/<int:id>/', article_detail_apiview),
    path('article_classapiview/', ArticleAPIView.as_view()),
    path('detail_classapiview/<int:id>/', ArticleDetailsAPIView.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('genericviewset/', include(router.urls)),
    path('genericviewset/<int:pk>/', include(router.urls)),
    path('modelviewset/', include(router.urls)),
    path('modelviewset/<int:pk>/', include(router.urls))
]
