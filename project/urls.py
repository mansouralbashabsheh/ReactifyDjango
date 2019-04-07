from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls import url
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    path('graphql', GraphQLView.as_view(graphiql=True)),

]