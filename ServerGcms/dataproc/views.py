from django.shortcuts import render
import os
from django.http import HttpResponse, JsonResponse
# Create your views here.

from rest_framework import generics
from google.cloud import storage
import os 

from google.oauth2 import service_account
import googleapiclient.discovery
from google.cloud import dataproc_v1


from google.cloud.dataproc_v1.gapic.transports import (
    cluster_controller_grpc_transport)
from google.cloud.dataproc_v1.gapic.transports import (
    job_controller_grpc_transport)



class ListClusters(generics.CreateAPIView):

    def post(self, request):
        print("List of clusters initiated ......")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\t\\keys.json"
        region = request.POST["region"]
        project_id = "deepak-cloud-trail"
        client_transport = (
            cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
                address='{}-dataproc.googleapis.com:443'.format(region)))

        dataproc_client = dataproc_v1.ClusterControllerClient(
            client_transport)
        
        list_clusters = dataproc_client.list_clusters(project_id, region)
        print(list_clusters)
        for cluster in list_clusters:
            print("$$$$$$$$", cluster.cluster_name)


def get_region_from_zone(zone):
    try:
        region_as_list = zone.split('-')[:-1]
        return '-'.join(region_as_list)
    except (AttributeError, IndexError, ValueError):
        raise ValueError('Invalid zone provided, please check your input.')

class CreateCluster(generics.CreateAPIView):

    def post(self, request):
        print("List of clusters initiated ......")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\t\\keys.json"
        project_id = "deepak-cloud-trail"
        zone = request.POST["zone"]
        region = get_region_from_zone(zone)
        zone_uri = \
        'https://www.googleapis.com/compute/v1/projects/{}/zones/{}'.format(
            project_id, zone)
        client_transport = (
            cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
                address='{}-dataproc.googleapis.com:443'.format(region)))

        dataproc_client = dataproc_v1.ClusterControllerClient(
            client_transport)
        cluster_name = request.POST["cluster_name"]
        cluster_data = {
        'project_id': project_id,
        'cluster_name': cluster_name,
        'config': {
            'gce_cluster_config': {
                'zone_uri': zone_uri
            },
            'master_config': {
                'num_instances': 1,
                'machine_type_uri': 'n1-standard-1'
            },
            'worker_config': {
                'num_instances': 2,
                'machine_type_uri': 'n1-standard-1'
                }
            }
        }
        cluster = dataproc_client.create_cluster(project_id, region, cluster_data)


