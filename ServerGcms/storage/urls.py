from django.urls import path
from .views import CreateBucket, ListBucket, SetIAMPolicy,RoleListView
urlpatterns = [
    path('bucket/', CreateBucket.as_view()),
    path('listbucket/', ListBucket.as_view()),
    path('updatepolicy/', SetIAMPolicy.as_view()),
    path('roleslist/', RoleListView.as_view())
 
]
