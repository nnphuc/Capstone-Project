from django.urls import path, include

from . import views

urlpatterns = [
    path('hello', views.sayhello, name='sayhello'),
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # add following lines to urlpatterns list
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
