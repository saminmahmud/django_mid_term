from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class add_musician(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class edit_musician(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class delete_musician (DeleteView):
    model = Musician
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    


def signup(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user_login')
        else: 
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('user_login')
    

class user_login(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    