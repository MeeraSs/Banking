from django.urls import path,include
from . import views
app_name = 'banking_app'
urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    # path('<slug:dist_slug>/', views.allDistricts,name='branches_by_districts'),
    # path('<slug:dist_slug>/<slug:branch_slug>/', views.branchDistrictDetail,name='branchDistrictDetail'),
    path('details/',views.details,name='details'),
]
