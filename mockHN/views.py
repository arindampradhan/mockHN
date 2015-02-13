from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from fancy_cache import cache_page
from yaaHN import hn_client
from datetime import datetime
from django.utils.timesince import timesince
from django.template import loader, Context
from .forms import RangeForm
from .helpers import icons


@cache_page(1800, remember_all_urls=True)
def home(request):
    from .helpers import icons
    topstories = list(hn_client.top_stories(33))
    return render(request, 'index.html', locals())


@cache_page(1800, remember_all_urls=True)
def page(request, num=1):
    from .helpers import icons
    if num == 2:
        first = 33
        last = 67
    if num == 3:
        first = 67
        last = 100
    else:
        first = None
        last = None
    topstories = list(hn_client.top_stories(limit=34, first=first, last=last))
    return render(request, 'index.html', locals())


@cache_page(1800, remember_all_urls=True)
def comment(request, comment_id=""):
    faces = range(39)
    comment = hn_client.get_comment(comment_id)
    time = datetime.fromtimestamp(comment.time)
    return render(request, 'comment.html', locals())


@cache_page(1800, remember_all_urls=True)
def story(request, story_id=""):
    story = hn_client.get_story(story_id)
    faces = range(39)
    time = datetime.fromtimestamp(story.time)
    return render(request, 'story.html', locals())


def story_handle(request):
    form = RangeForm()
    if request.method == "POST":
        form = RangeForm(request.POST)
        if form.is_valid():
            obj = form.cleaned_data
            num = obj.get('num')
            topstories = hn_client.top_stories_ids()
            select_id = topstories[num]
            return HttpResponseRedirect('/story/{}'.format(select_id))
        else:
            form.error
        return render(request, 'index.html', locals())

# @cache_page(1800, remember_all_urls=True)
# def comment(request, comment_id=""):
#     comments = hn_client.get_comments(comment_id)
#     return render(request, 'comment.html', locals())


@cache_page(1800, remember_all_urls=True)
def user(request, user_id=""):
    faces = range(39)
    user = hn_client.get_user(user_id)
    created = datetime.fromtimestamp(user.created)
    return render(request, 'user.html', locals())
