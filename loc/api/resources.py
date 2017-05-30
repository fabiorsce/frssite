from tastypie import fields
from tastypie.resources import ModelResource
from loc.models import Material, Review, ReviewStatus
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication,SessionAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization


class FieldSelectionMixin(object):
    """
    add ability to Resource to query specific fields. This works by
    removing any fields not in the fields list provided by the fields
    query parameter. 
    
    Programming Use:
       class MyResource(FieldSelectionMixin, ModelResource):
           ...
           (as with any normal resource)
    
    API Use: 
       /my/api/myresource/?fields=field[,field[, ...]]
       /my/api/myresource/<pk>?fields=field[,field[, ...]]
       
    For debugging purpose, add &fields_debug=1 to retrieve the list
    of fields removed and those actually selected:
    
       {
         '_fields_removed' : [ 'field1', 'field2', ... ],
         '_fields_selected' : [ 'field1', 'field2', ... ],
         <actual data>
       }
    """
    def dehydrate(self, bundle):
        """
        remove fields not requested
        
        note: this is called for every object, so works for both detail and
              list requests
        """
        only_fields = bundle.request.GET.get('fields')
        debug_fields = bundle.request.GET.get('fields_debug', False)
        if only_fields:
            only_fields = only_fields.split(',')
            fields_to_remove = [field for field in bundle.data.keys() 
                                if field not in only_fields]
            for field in fields_to_remove:
                del bundle.data[field]
            if debug_fields:
                bundle.data['_fields_selected'] = [field for field in only_fields 
                                                   if field in bundle.data.keys()]
                bundle.data['_fields_removed'] = fields_to_remove
        return bundle


class UserResource(FieldSelectionMixin, ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name']
        allowed_methods = ['get']
        filtering = {
            'username': ['exact'],
        }

class MaterialResource(FieldSelectionMixin, ModelResource):
    class Meta:
        queryset = Material.objects.all()
        resource_name = 'material'
        allowed_methods = ['get']
        filtering = {
            'serial_number': ['exact'],
        }

        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

class ReviewStatusResource(FieldSelectionMixin, ModelResource):
    class Meta:
        queryset = ReviewStatus.objects.all()
        resource_name = 'review_status'
        allowed_methods = ['get']
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()

class ReviewResource(FieldSelectionMixin, ModelResource):

    user = fields.ForeignKey(UserResource, 'user')
    material = fields.ForeignKey(MaterialResource, 'material')
    status = fields.ForeignKey(ReviewStatusResource, 'status')

    class Meta:
        queryset = Review.objects.all()
        resource_name = 'review'
        allowed_methods = ['get', 'post']

        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication(), SessionAuthentication())
        #authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True


