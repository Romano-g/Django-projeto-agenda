from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # contact CRUD (CreateReadUpdateDelete)
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/read/', views.contact, name='contact'),
]
