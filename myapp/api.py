# myapp/api.py
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
# from tastypie.authorization import Authorization
from tastypie.authentication import OAuthAuthentication
from tastypie.authorization import DjangoAuthorization
from myapp.models import Entry


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = OAuthAuthentication()
        authorization= DjangoAuthorization()


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        allowed_methods = ['get','put','post','update','delete']
        authentication = OAuthAuthentication()
        authorization= DjangoAuthorization()
