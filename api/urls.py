from django.urls import path,include
from . import views
  
urlpatterns = [
    
    path('',views.ApiOverview, name="api-overview"),
    path('enroll-list/',views.enrolllist, name="enroll-list"),
    path('enroll-detail/<str:username>/',views.enrollDetail, name="enroll-detail"),
    path('enroll-register/',views.enrollRegister, name="enroll-register"),
    path('enroll-update/<str:username>/',views.enrollUpdate, name="enroll-update"),
    path('enroll-delete/<str:username>',views.enrollDelete, name="enroll-delete"),
    path('enroll-view/<str:user_type>/',views.enrollHolder, name="holder"),
    path('enroll-login',views.enrollLogin, name="enroll-login"),

    path('project-log/',views.projectlog, name="project-log"),
    path('project-create/',views.projectCreate, name="project-create"),
    path('project-detail/<str:name>/',views.projectDetail, name="project-detail"),
    path('project-view/<str:username>/',views.projectHolder, name="holder"),
    path('project-edit/<str:name>/',views.projectEdit, name="project-edit"),
    path('project-delete/<str:name>',views.projectDelete, name="project-delete"),

    path('task-record/',views.taskrecord, name="task-record"),
    path('task-create/',views.taskCreate, name="task-create"),
    path('task-detail/<str:title>/',views.taskDetail, name="task-detail"),
    path('task-update/<str:title>/',views.taskUpdate, name="task-title"),
    path('task-view/<str:project>',views.taskHolder, name="holder"),
    path('task-delete/<str:title>',views.taskDelete, name="task-title"),
    path('task-status/<str:status>',views.taskStatus, name="status"),
    path('task-track/',views.taskTrack, name="track"),

    path('bug-record/',views.bugrecord, name="bug-record"),
    path('bug-create/',views.bugCreate, name="bug-create"),
    path('bug-detail/<str:head>/',views.bugDetail, name="bug-detail"),
    path('bug-update/<str:head>/',views.bugUpdate, name="bug-update"),
    path('bug-delete/<str:head>',views.bugDelete, name="bug-delete"),
    path('bug-track/<str:task>',views.bugTrack, name="bug-track"),
]
