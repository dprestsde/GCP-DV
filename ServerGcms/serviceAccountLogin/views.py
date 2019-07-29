from django.shortcuts import render
import os
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from google.cloud import storage
import os 
from django.http import JsonResponse

class CreateServiceAccount(generics.CreateAPIView):

    def post(self, request):
        name = request.POST["name"]
        os.system("gcloud iam service-accounts create " + name)
        project_id = request.POST["id"]
        role_type = request.POST["role"]
        print(role_type)
        print("gcloud projects add-iam-policy-binding {} --member 'serviceAccount:{}@{}.iam.gserviceaccount.com' --role 'roles/{}' ".format(project_id, name, project_id, role_type))
        print("Created Successfully")
        



class UserServiceAccount(generics.CreateAPIView):

    def post(self, request):
        name = request.POST["name"]
        project_id = request.POST["id"]
        os.system("gcloud iam service-accounts keys create keys.json --iam-account {}@{}.iam.gserviceaccount.com".format(name, project_id))
        print("User Logged In")