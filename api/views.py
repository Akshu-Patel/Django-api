from pickle import FALSE
from subprocess import CompletedProcess
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# from django.contrib.auth.models import Enroll
from django.contrib.auth import authenticate
from .serializers import EnrollSerializer,ProjectSerializer,TaskSerializer
from rest_framework import status
from datetime import datetime


from .models import *
from .serializers import *

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List':'enroll-list',
        'Detail View':'enroll-detail/<str:username>/',
        'Register': '/enroll-register/',
        'Update': 'enroll-update/<str:username>/',
        'Delete': 'enroll-delete/<str:username>',
        'Holder':'enroll-view/<str:user_type>/',
        'Login': '/enroll-login/',

        'Log':'project-log',
        'Create': '/project-create/',
        'Detail View':'project-detail/<str:name>/',
        'Holder':'project-view/<str:username>/',
        'Delete': 'project-delete/<str:name>',
        'Edit': 'project-edit/<str:name>/',

        'Record':'task-record',
        'Create': '/task-create/',
        'Update': 'task-update/<str:title>/',
        'Detail View':'task-detail/<str:name>/',
        'Delete': 'task-delete/<str:pk>',
        'Holder':'task-view/<str:project>',
        'Status':'task-status/<str:status>',
        'Track':'task-track/',
        # 'Project': '/enroll-project/'

        'Record':'bug-record',
        'Create':'/bug-create/',
        'Update':'bug-update/<str:head>/',
        'Detail View':'bug-detail/<str:head>/',
        'Delete':'bug-delete/<str:head>',
        'Track':'bug-view/<str:task>',

}

@api_view(['GET'])
def enrolllist(request):
    print("list view")
    enrolls = Enroll.objects.all()
    serializer = EnrollSerializer(enrolls, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def enrollDetail(request,username):
    # print("inside the api")
    enrolls = Enroll.objects.get(username=username)
    serializer = EnrollSerializer(enrolls, many=False)
    return Response(serializer.data)

    
@api_view(['POST'])
def enrollRegister(request):
    print(request.data)
    serializer = EnrollSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return HttpResponse(status=404)


@api_view(['POST'])
def enrollUpdate(request, username):
    enroll = Enroll.objects.get(username=username)
    serializer = EnrollSerializer(instance=enroll,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def enrollDelete(request,username):
    enroll = Enroll.objects.get(username = username)
    enroll.delete()
    return Response('Item successfully deleted!')

@api_view(['GET'])
def enrollHolder(request,user_type):
    #print("inside the api")
    enrollsData = Enroll.objects.filter(user_type=user_type)
    #print('enrolls',enrollsData)
    list = []
    for user in enrollsData:
        serializer = EnrollSerializer(user, many=False)
        list.append(serializer.data)
    return Response(list)    


# @api_view(['DELETE'])
# def enrollDelete(request):
#     print("enroll abc")
#     print(request.data)
#     enroll = Enroll.objects.get(username = request.data["username"])
#     enroll.delete()
#     return Response('Item successfully deleted!')  
   
@api_view(['POST'])
def enrollLogin(request):
    print("Request Data looking like ", request.data)
    print("Request Data looking like ", request.data["email"])
    print("Request Data looking like ", request.data["password"])
    print("Request Data looking like ", request.data["user_type"])


    print("hello")
    # fields = ('email', 'password')
    # obj = {"email" : request.data["email"]}

    try:
        enrollLogin = Enroll.objects.get(email = request.data["email"])
        # enrollLogin = Enroll.objects.get(email = request.data["password"])
        #enrollLogin = Enroll.objects.get(user_type = request.data["user_type"])
        print (enrollLogin.email)
        print (enrollLogin.password)
        print (enrollLogin.user_type)

        
        role=enrollLogin.user_type
        return HttpResponse(role)

    except Exception as E:
        print (E)
        return HttpResponse (status = 404)

@api_view(['GET'])
def projectlog(request):
    print("log view")
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projectDetail(request,name):
    # print("inside the api")
    projects = Project.objects.get(name=name)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return HttpResponse(status=404)

@api_view(['POST'])
def projectEdit(request,name):
    project = Project.objects.get(name=name)
    serializer = ProjectSerializer(instance=project,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def projectDelete(request,name):
    # print("enroll abc")
    # print(request.data)
    project = Project.objects.get(name = name)
    project.delete()
    return Response('Item successfully deleted!')

@api_view(['GET'])
def projectHolder(request,username):
    # print("inside the api")
        user = Project.objects.filter(project_manager = username)
        list=[]
        for projects in user:
            serializer = ProjectSerializer(projects, many=False)
            list.append(serializer.data)
        return Response(list)

@api_view(['GET'])
def taskrecord(request):
    print("record view")
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return HttpResponse(status=404)

@api_view(['POST'])
def taskUpdate(request,title):
    task = Task.objects.get(title=title)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,title):
    # print("inside the api")
    tasks = Task.objects.get(title=title)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,title):
    # print("enroll abc")
    # print(request.data)
    task = Task.objects.get(title = title)
    task.delete()
    return Response('Item successfully deleted!')

@api_view(['GET'])
def taskHolder(request,project):
    # print("inside the api")
        projectdata = Task.objects.filter(project = project)
        show=[]
        for tasks in projectdata:
            serializer = TaskSerializer(tasks, many=False)
            show.append(serializer.data)
        return Response(show)
   
@api_view(['GET'])
def taskStatus(request,status):
    # print("inside the api")
        status = Task.objects.filter(status=status)
        show=[]
        for tasks in status:
            serializer = TaskSerializer(tasks, many=False)
            show.append(serializer.data)
        return Response(show)

@api_view(['GET'])
def taskTrack(request):
        status = Task.objects.filter(completed="False")
        show=[]
        for tasks in status:
            serializer = TaskSerializer(tasks, many=False)
            show.append(serializer.data)
        return Response(show)

@api_view(['GET'])
def bugrecord(request):
    print("record view")
    bugs = Bug.objects.all()
    serializer = BugSerializer(bugs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def bugCreate(request):
    serializer = BugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return HttpResponse(status=404)

@api_view(['POST'])
def bugUpdate(request,head):
    bug = Bug.objects.get(head=head)
    serializer = BugSerializer(instance=bug,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def bugDetail(request,head):
    # print("inside the api")
    bugs = Bug.objects.get(head=head)
    serializer =BugSerializer(bugs, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def bugDelete(request,head):
    # print("enroll abc")
    # print(request.data)
    bug = Bug.objects.get(head = head)
    bug.delete()
    return Response('Item successfully deleted!')

@api_view(['GET'])
def bugTrack(request,task):
    # print("inside the api")
        taskdata = Bug.objects.filter(task = task)
        show=[]
        for bugs in taskdata:
            serializer = BugSerializer(bugs, many=False)
            show.append(serializer.data)
        return Response(show)