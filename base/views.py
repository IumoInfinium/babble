from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Post
from .serializers import PostSerializer
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    return render(request, 'login.html')

def join(request):
    return render(request,'join.html')
    
def public_feed(request):
    # posts = Post.objects.all().order_by('-created')
    print(request.COOKIES)
    room_code = request.COOKIES.get('channel_id')
    print(room_code)
    posts = Post.objects.filter(channel_id__exact=room_code).order_by('-created')
    print(posts)
    context = {'posts':posts}
    return render(request, 'feed.html', context)

@api_view(['POST'])
def add_post(request):
    data = request.data 
    post = Post.objects.create(
        sender=data['sender'],
        body=data['body'],
        channel_id=data['channel_id']
    )
    serializer  = PostSerializer(post, many=False)
    return Response(serializer.data)