from django.urls import path

from . import views

urlpatterns = [
    path('', views.LandPage, name='landpage'),
    path('write-text',views.WriteText,name='WriteText'),
    path('translate-text', views.TranslateText, name='TranslateText'),
    path('upload-file',views.UploadFile,name='UploadFile'),
    path('translate-file', views.TranslateFile, name='TranslateFile'),

]