from django.contrib import admin
from django.urls import path, include
from accounts.views import user_login, edit
from django.contrib.auth import views as auth_views
from devicetoserver import urls
import devicetoserver, accounts, modelselection
from serverdata import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .api import router
from .apirep import routerep
from allauth.account.views import confirm_email
from django.views.generic import TemplateView 
from django.conf.urls import url

urlpatterns = [
    path('admin/filebrowser/', include('filebrowser.urls')),
    path('admin/log_viewer/', include('log_viewer.urls')),
    path('admin/', admin.site.urls), 
    path('', include('devicetoserver.urls')),
    path('accounts/', include('accounts.urls')),
    path('modelselection/', include('modelselection.urls')),    
    path('computervision/', include('computervision.urls')),
    path('api/sensoviz/', include(router.urls)),
    path('api/v1/', include(routerep.urls)),
    path('report/', include('fesibility.urls')),
    path('supportsystem/', include('supportsystem.urls')),
    path('openvino/', include('openvinofreezed.urls')),
    path('softwareactivation/', include('softwareactivation.urls')),
    path('instancesegmentation/', include('instancesegmentation.urls')),
    path('sensovisionshop/', include('ecommerce_app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('inventory/', include('inventory.urls')),
    path('salerecord/', include('salesapp.urls')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    path('allaccounts/', include('allauth.urls')),
    path('hr/', include('hiring.urls')),

    path('account/', include('accountant.urls', namespace='account')),
#    path('chat/', include('core.urls')),
    path('analytics/', include('analytics.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('orders/', include('orders.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Sensovision"
admin.site.site_title = "Sensovision Portal"
admin.site.index_title = "Welcome to Sensovision"