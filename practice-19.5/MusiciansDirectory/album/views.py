
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Album
from .forms import AlbumForm


@method_decorator(login_required, name='dispatch')
class add_album(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class edit_album(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


