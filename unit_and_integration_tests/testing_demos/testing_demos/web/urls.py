from django.urls import path

from testing_demos.web.views import ProfileCreateView, ProfileListView, ProfileDetailsView

urlpatterns = (
    path('', ProfileListView.as_view(), name='list profiles'),
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='details profile'),
)