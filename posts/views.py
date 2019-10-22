from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,ProfileForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import User


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
    current_user = request.user
    date = dt.date.today()
    images = Image.get_image()
    comment = Comment.objects.all()

    for image in images:
        comments = Comment.objects.filter(image=image)
        print(comments)


    # comment = Comment.objects.filter(id = current_user.id).first()
    # print(comment)
    return render(request, 'all-posts/posts-today.html', {"date": date,"images": images, 'comments':comments})



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
    current_user = request.user
    images = Image.objects.filter(user=current_user)
    profilepicture=Profile.objects.get(user=current_user)
   
 
    return render(request, 'all-posts/profiledisplay.html', {"profilepicture": profilepicture,"images":images})



def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users= Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-posts/search.html',{"searched_users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-posts/search.html',{"message":message})


# def register(request):
    
#     if request.method == 'POST':
#         form =  UserCreationForm(request.POST)
#         if form.is_valid():
#            form.save()
#         return redirect('profiledisplay')

#     else:
#         form = UserCreationForm()
#         args={"form":form}
#     return render(request, 'registration/registration_form.html', {"form": form})


@login_required(login_url='/accounts/login/')
def commenting(request,image_id):
    current_user = request.user
    if request.method == 'POST':
        imagetocomment = Image.objects.filter(id = image_id).first()
        # user = User.objects.filter(user = current_user.id).first()
        # print(user)
        form =  CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user= current_user
            comment.image =imagetocomment
            comment.save()
        return redirect('postsToday')

    else:
        form = CommentForm()
    return render(request, 'all-posts/comment-form.html', {"form": form, 'image_id':image_id})
