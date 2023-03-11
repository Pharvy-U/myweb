from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:id>', views.blog_single, name='get-blog'),
    path('project/<str:id>', views.project_single, name='get-project'),
    path('mail-me/', views.sendMail, name='mail'),

    # CRUD
    path('new-project', views.create_project, name='create-project'),
    path('update-project/<str:id>', views.update_project, name='update-project'),
    path('delete-project/<str:id>', views.delete_project, name='delete-project'),
    path('new-blog', views.create_blog, name='create-blog'),
    path('update-blog/<str:id>', views.update_blog, name='update-blog'),
    path('delete-blog/<str:id>', views.delete_blog, name='delete-blog'),

    # Authentication
    path('control/', views.control_panel, name='control'),
    path('logout/', views.logout_user, name="logout"),
    # blog single
    # portfolio single
]