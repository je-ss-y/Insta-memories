from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required


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

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day



# def past_days_posts(request,past_date):

#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
