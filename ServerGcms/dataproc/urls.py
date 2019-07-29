from django.urls import path
from .views import ListClusters,CreateCluster


urlpatterns = [
  path('listclusters/', ListClusters.as_view()),
  path('createcluster/', CreateCluster.as_view())
]
