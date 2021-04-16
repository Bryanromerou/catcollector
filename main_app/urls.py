from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/new/', views.add_cat, name='add_cat'),
    path('cats/<int:cat_id>/', views.cats_detail, name="detail"),
    path('cats/<int:cat_id>/edit/', views.edit_cat, name="edit_cat"),
    path('cats/<int:cat_id>/delete/', views.delete_cat, name="delete_cat"),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('profile/', views.show_profile, name='show_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('accounts/signup/', views.signup, name='signup'),
]