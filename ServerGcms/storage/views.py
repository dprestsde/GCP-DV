from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework import generics
from google.cloud import storage
import os 

from google.oauth2 import service_account
import googleapiclient.discovery

class CreateBucket(generics.CreateAPIView):

    def post(self, request):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\t\\keys.json"
        storage_client = storage.Client()
        print("Instance Created")
        print(request.POST["name"])
        bucket = storage_client.bucket(request.POST["name"])
        print("Bucket Created")
        bucket.location = request.POST["location"]
        print("Loaction")
        if request.POST["storage_class"] != "global":
            bucket.storage_class = request.POST["storage_class"]
        print("Storage Class")
        bucket.create()

        return HttpResponse("<h1> Bucket Created</h1>")


class ListBucket(generics.CreateAPIView):

    def post(self, request):
        print("###########")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\t\\keys.json"
        client = storage.Client()
        print("CLIENTSSERVER")
        buckets = client.list_buckets()
        list_of_bucket = []
        for i in buckets:
            list_of_bucket.append({"name":i.name, "Location":i.location, "storage_class":i.storage_class} )
        print(list_of_bucket)
        return JsonResponse(list_of_bucket, safe=False)

class RoleListView(generics.CreateAPIView):
  
    def post(self, request):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\t\\keys.json"

        credentials = service_account.Credentials.from_service_account_file(
        filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    # Create the Cloud IAM service object
        service = googleapiclient.discovery.build(
            'iam', 'v1', credentials=credentials) 
        body = {
            "fullResourceName": "//cloudresourcemanager.googleapis.com/projects/deepak-cloud-trail"
        }
        response = service.roles().queryGrantableRoles(body=body).execute()
        roles = response['roles']
        ListRoles = []
    # Process the response
        for role in roles:
            ListRoles.append({"Name": role["title"], "title":role["name"]})

        return JsonResponse(ListRoles, safe=False)
            



class SetIAMPolicy(generics.CreateAPIView):

    def post(self, request):
        print("$$$$$$")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\t\\keys.json"
        bucket_name = request.POST["Bucket_Name"]
        role = request.POST["role"]
        member = request.POST["member"]
        print(type(bucket_name))
        print(type(role))
        print(type(member))
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        policy = bucket.get_iam_policy()
        policy[role].add(member)
        print("{{{{{{{{{{")
        bucket.set_iam_policy(policy)
        print("}}}}}}}}}}}}}}")
        for i in policy:
            print(i, policy[i])
        
        return JsonResponse("Successfully Updated", safe=False)

