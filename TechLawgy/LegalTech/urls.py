from django.urls import path
from . import views
urlpatterns = [
    
    
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login-form",views.login_form, name="login_form"),
    path("inner-page",views.inner_page, name="inner_page"),
    path("click_me",views.click_me, name="click_me"),
    

    path('view_cases', views.view_cases, name="view_cases"),
    path('register_case', views.register_case, name="register_case"),


    path('signup', views.signup_view, name="signup"),
    path('logout_session',views.logout_session,name='logout_session'),
    path('activation_sent', views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),

    
    

    

    
]