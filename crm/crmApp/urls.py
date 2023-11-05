from django.urls import path
from crmApp.views import home,add_cv,delete_cv,update_cv,login_page,logout_page,register_page,record

urlpatterns = [
    path('home/',home,name='home'),
    path('add-cv/',add_cv.as_view(),name='add-cv'),
    path('delete-cv/',delete_cv.as_view(),name='delete-cv'),
    path('update-cv/<int:id>',update_cv.as_view(),name='update-cv'),
    path('record/<int:id>',record,name='record'),
    
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logut'),
    path('register/',register_page,name='register')
    ]