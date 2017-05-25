from tastypie.resources import ModelResource
from loc.models import Material


class MaterialResource(ModelResource):
    class Meta:
        queryset = Material.objects.all()
        allowed_methods = ['get']
        filtering = {
            'serial_number': ['exact'],
        }
