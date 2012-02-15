from tastypie.resources import ModelResource
from projects.models import Project
from users.models import UserProfile
from schools.models import School

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.get_popular()
        fields = ['name', 'category']

class UserProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        fields = ['username', 'bio', 'image']

class SchoolResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
