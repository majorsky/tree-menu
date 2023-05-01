from django.conf.urls import url
from accord_menu.views import IndexView
# from menus.views import menu_item

app_name = 'accord_menu'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(.*)/$', IndexView.as_view(), name='index'),
]
