from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('items/', views.items, name='items'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    #add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit
    path('update/<int:id>',views.update_item,name='update_item'),
    #Delete
    path('delete/<int:id>',views.delete_item,name='delete_item'),
]
