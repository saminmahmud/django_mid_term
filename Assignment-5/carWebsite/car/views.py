from django.shortcuts import render,redirect
from .forms import RegisterForm,EditForm , CommentForm
from django.views.generic import  UpdateView,DetailView
from django.urls import reverse_lazy
from .models import Car, Comment, Profile
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
    
class LogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    
@method_decorator(login_required, name='dispatch')
class edit_profile(UpdateView):
    model = User
    form_class = EditForm
    template_name = 'edit_profile.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')



class DetailPostView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'cardetails.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object() 
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car  
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all() 
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


@login_required
def buy(request, id):
    car = Car.objects.get(pk=id)
    car.quantity -= 1
    car.save()
    # user_profile = profile.objects.get(request.user) 
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    user_profile.cars.add(car)
    return redirect('profile')

# ekhaneo required dite hobe
@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    cars = user_profile.cars.all()
    return render(request, 'profile.html', {'cars': cars})


