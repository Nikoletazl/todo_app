from django.urls import path

from tools.web.views import index, ProfilesListView

urlpatterns = (
    path('', index, name='index'),
    path('profiles/', ProfilesListView.as_view(), name='profiles'),
)

import tools.web.signals