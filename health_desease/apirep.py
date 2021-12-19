from rest_framework import routers
from health import api_views as hire_viewed

routerep = routers.DefaultRouter()
routerep.register(r'patient', hire_viewed.PatientViewset)
