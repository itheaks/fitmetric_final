from django import forms
from .models import BlogPost
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['image', 'title', 'description', 'event_date', 'location', 'duration', 'timing']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Event Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Event Description'
        self.fields['event_date'].widget.attrs['placeholder'] = 'Event Date (YYYY-MM-DD)'
        self.fields['location'].widget.attrs['placeholder'] = 'Event Location (City)'
        self.fields['duration'].widget.attrs['placeholder'] = 'Event Duration (In Hours)'
        self.fields['timing'].widget.attrs['placeholder'] = 'Event Timing (HH:MM) 24-Hour Format'

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        # add user to form before saving
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('list_blog_post')
    else:
        form = BlogPostForm()
    return render(request, 'events/index.html', {'form': form})

@login_required
def event_list(request):
    events = BlogPost.objects.filter(is_active=True).order_by('-event_date')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def EventsSearch(request):
    search_query = request.GET.get('search', '')
    videos = BlogPost.objects.filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(location__icontains=search_query)
    ).values('title', 'description', 'event_date', 'location', 'duration', 'timing','image')
    video_list = list(videos)
    return JsonResponse(video_list, safe=False)