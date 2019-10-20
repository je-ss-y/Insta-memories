from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,ProfileForm
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = current_user
            article.save()
        return redirect('postsToday')

    else:
        form =NewImageForm()
    return render(request, 'all-posts/onepost.html', {"form": form})
# Create your views here.
@login_required(login_url='/accounts/login/')
def posts_of_day(request):
    date = dt.date.today()
    image = Image.objects.all()
    return render(request, 'all-posts/posts-today.html', {"date": date,"image": image})



# View Function to present posts from past days
def past_days_posts(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(postsToday)

    return render(request, 'all-posts/past-posts.html', {"date": date})


@login_required(login_url='/accounts/login/')
def profile_form(request):
    current_user = request.user
    if request.method == 'POST':
        form =  ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = ProfileForm()
    return render(request, 'all-posts/profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user_profile(request):
    profilepicture=Profile.objects.all()
    args={"profilepicture":profilepicture}
    return render(request, 'all-posts/profiledisplay.html', {"profilepicture": profilepicture})



def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users= Image.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html',{"profile": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})


def register(request):
    
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('all-posts/posts-today')

    else:
        form = UserCreationForm()
        args={"form":form}
    return render(request, 'registration/registration_form.html', {"form": form})
