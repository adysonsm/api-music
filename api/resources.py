from tastypie.resources import ModelResource
from api.models import Track

class TrackResource(ModelResource):
    class Meta:
        queryset = Track.objects.all()
        resource_name = 'music'
