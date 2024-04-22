from django import forms
from .models import BlogPost
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['image', 'title', 'description', 'event_date', 'location', 'duration', 'timing']


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_blog_post')
    else:
        form = BlogPostForm()
    return render(request, 'events/index.html', {'form': form})

def event_list(request):
    events = BlogPost.objects.filter(is_active=True).order_by('-event_date')
    print(events)
    return render(request, 'events/event_list.html', {'events': events})


def EventsSearch(request):
    search_query = request.GET.get('search', '')
    videos = BlogPost.objects.filter(
        Q(title__icontains=search_query)
    ).values('title', 'description', 'event_date', 'location', 'duration', 'timing','image')
    video_list = list(videos)
    return JsonResponse(video_list, safe=False)