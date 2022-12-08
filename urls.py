from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from author import views as author_views

	@@ -32,4 +33,5 @@
    path('api/', include(router.urls)),
    path('api/todo/', author_views.TodoModelAPIView.as_view()),
    path('api/todo/<int:pk>', author_views.TodoModelAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token)