from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path("", MyView.as_view(), name="home"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("history/", History.as_view(), name="history"),
    path("register/", RegisterUser.as_view(), name="register"),
    path('download-archive/<int:record_id>/', DownloadArchiveView.as_view(), name='download_archive'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
