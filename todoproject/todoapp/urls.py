from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<taskid>/',views.delete,name='delete'),
    path('update/<taskid>/',views.update,name='update'),
    path('homeView/',views.homeView.as_view(),name='homeView'),
    path('detailView/<int:pk>/',views.detailView.as_view(),name='detailView'),
    path('updateView/<int:pk>/',views.updateView.as_view(),name='updateView'),
    path('deleteView/<int:pk>/',views.deleteView.as_view(),name='deleteView')
]
