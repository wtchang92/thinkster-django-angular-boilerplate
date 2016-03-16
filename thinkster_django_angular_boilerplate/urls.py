from django.conf.urls import patterns, url, include

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework_nested import routers

from authentication.views import AccountViewSet

from authentication.views import LoginView

from authentication.views import LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'api_accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url('^.*$', IndexView.as_view(), name='index'), #This is known as a passthrough or catch-all route. It accepts all requests not matched by a previous rule and passes the request through to AngularJS's router for processing. The order of other URLS is normally insignificant.
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

