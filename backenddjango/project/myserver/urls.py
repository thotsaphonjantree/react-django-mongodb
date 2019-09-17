from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from project.myserver.views import *
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')

merouter = merouters.DefaultRouter()
merouter.register(r'student', StudentViewSet)
merouter.register(r'major', MajorViewSet)
merouter.register(r'studentbymajor/(?P<major_id>.+)', StudentByMajorViewSet,basename='Student')

urlpatterns = [
url(r'^docs/', schema_view),
]

urlpatterns += merouter.urls    