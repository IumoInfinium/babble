from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Post,Room
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
    # print(request.COOKIES)
    room_code = request.COOKIES.get('channel_id')
    # print(room_code)
    posts = Post.objects.filter(channel_id__exact=room_code).order_by('-created')
    # print(posts)
    context = {'posts':posts}
    return render(request, 'feed.html', context)

@api_view(['POST'])
def create_room(request):
    request_data = request.data
    
    try:
        room_info = Room.objects.create(
            created_by=request_data['created_by'],
            room_code = request_data['room_code']
        )
        room_info.save()
        # print(request_data)
        return Response({'result':'true'})
    except:
        return Response({'result':'false'})

@api_view(['POST'])
def check_code(request):
    request_data = request.data
    # print(request_data)
    all_rooms = Room.objects.values('room_code').distinct()
    # print(all_rooms)
    for room in all_rooms:
        if(room['room_code'] == request_data['join_code']):
            return Response({'result':'true'})
    return Response({'result':'false'})

@api_view(['POST'])
def add_post(request):
    data = request.data 
    post = Post.objects.create(
        sender=data['sender'],
        body=data['body'],
        channel_id=data['channel_id']
    )
    serializer  = PostSerializer(post, many=False)
    # print(serializer.data)
    return Response(serializer.data)