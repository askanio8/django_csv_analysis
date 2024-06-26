from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import DownloadArchiveView, History, LoginUser, MyView, RegisterUser, logout_user

urlpatterns = [
    path("", MyView.as_view(), name="home"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("history/", History.as_view(), name="history"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("download-archive/<int:record_id>/", DownloadArchiveView.as_view(), name="download_archive"),
    path("generate-html/", MyView.generate_ydata_html, name="generate_ydata_html"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
