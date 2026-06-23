from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'student-register/',
        views.student_register,
        name='student_register'
    ),

    path(
        'student-login/',
        views.student_login,
        name='student_login'
    ),

    path(
        'admin-login/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'student-dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'search-company/',
        views.search_company,
        name='search_company'
    ),

    path(
        'company/<int:company_id>/',
        views.company_detail,
        name='company_detail'
    ),

    path(
        'add-company/',
        views.add_company,
        name='add_company'
    ),

    path(
        'update-company/<int:company_id>/',
        views.update_company,
        name='update_company'
    ),

    path(
        'delete-company/<int:company_id>/',
        views.delete_company,
        name='delete_company'
    ),

    path(
        'view-companies/',
        views.view_companies,
        name='view_companies'
    ),

    path(
        'eligibility/',
        views.eligibility,
        name='eligibility'
    ),

    path(
        'deadlines/',
        views.deadlines,
        name='deadlines'
    ),

    path(
        'sort-package/',
        views.sort_package,
        name='sort_package'
    ),

    path(
        'placement-report/',
        views.placement_report,
        name='placement_report'
    ),

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),
]