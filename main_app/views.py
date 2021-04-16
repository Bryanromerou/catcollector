from django.conf import settings
from django.shortcuts import render, redirect
from .models import Cat, Profile
from .forms import FeedingForm, CatForm, ProfileForm, ProfileForm2
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def about(request):
  return render(request,'about.html')

def add_cat(request):
  form = CatForm(request.POST or None)

  if request.method == 'POST' and form.is_valid():
    new_cat = form.save(commit=False)
    new_cat.user = request.user
    new_cat.save()
    return redirect('detail',cat_id=new_cat.id)
  else:
    print("this is a get request")
    cat_form = CatForm()
    return render(request,'cats/new.html',{'cat_form': cat_form})

def cats_index(request):
  cats = Cat.objects.filter(user=request.user)
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request,cat_id):
  print(request.user.id)
  cat = Cat.objects.get(id=cat_id)
  print(cat.feeding_set.all())
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', { 'cat': cat , 'feeding_form': feeding_form})

def edit_cat(request,cat_id):
  cat = Cat.objects.get(id=cat_id)
  if request.method == 'POST':
    cat_form = CatForm(request.POST, instance=cat)
    if cat_form.is_valid():
      cat_form.save()
      return redirect('detail', cat_id=cat_id)
  else:
    cat_form = CatForm(instance=cat)
    context = {"form": cat_form}
    return render(request,'cats/edit.html',context)

def delete_cat(request,cat_id):
  Cat.objects.filter(id=cat_id).delete()
  return redirect('index')

# add this new function below cats_detail
def add_feeding(request, cat_id):
   # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

def signup(request):
  error_message = ''
  user_form = UserCreationForm(request.POST or None)
  profile_form = ProfileForm2(request.POST or None)
  if request.method == 'POST':
    if profile_form.is_valid():
      email = request.POST.get("email")
      match = Profile.objects.filter(email = email)
      if match.exists():
        error_message = "There is already a user with this email address"
      elif user_form.is_valid():  
        user = user_form.save()
        profile = Profile(user = user, name = request.POST.get("name"), email = email)
        profile.save()
        login(request,user)
        subject = 'Email Comfirmation for catcollector!'
        message = 'Thank you for signing up for the catcollector we value your business.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [email,from_email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect('index')
      else:
        error_message = "Invalid Sign Up Try again"

  # This should not be executed if the form was valid, However if it is invalid then we should pick up the error along the 
  # way otherwise if the request is not a post it shall skip both of the if statements above.
  context = { 'form': user_form, 'error_message': error_message, 'profile_form':profile_form}
  return render(request,'registration/signup.html',context)

def show_profile(request):
  profile = Profile.objects.get(user=request.user)
  print(profile)
  return render(request,'profile/show.html',{'profile':profile})

def edit_profile(request):
  profile = Profile.objects.get(user=request.user)
  if request.method == 'POST':
    form = ProfileForm(request.POST,instance=profile)
    if form.is_valid():
      form.save()
      return redirect('show_profile')

  form = ProfileForm(instance=profile)
  return render(request,'profile/edit.html',{'form':form})