from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from testing_demos.web.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            context['user'] = self.request.user.username
        else:
            context['user'] = 'No user'

        return context


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/details.html'
