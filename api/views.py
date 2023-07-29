from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post,Comment,Profile,Like,Follow
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import commentSerilizers,postSerilizers,profileSerilizers,LikeSerilizers,followSerilizers
from django.contrib.auth.models import User

class postviewSets(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=postSerilizers
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    @action(methods=['POST'],detail=True)
    def post_like(self, request, pk=None):
        if 'like' in request.data:
            post = Post.objects.get(id=pk)
            like = request.data['like']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                add_like= Like.objects.get(user=user.id, post=post.id) 
                add_like.like= like
                add_like.save()
                serializer =LikeSerilizers(add_like, many=False)
                json = {
                    'message': 'successfully added !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                add_like = Like.objects.create(like=like,post=post, user=user)
                serializer=LikeSerilizers(add_like, many=False)
                json = {
                    'message': 'Like is created !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

class commentviewSets(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=commentSerilizers
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    @action(methods=['POST'],detail=True)
    def comment_like(self, request, pk=None):
        if 'like' in request.data:
            comment = Comment.objects.get(id=pk)
            like = request.data['like']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                add_like= Like.objects.get(user=user.id, comment=comment.id) 
                add_like.like= like
                add_like.save()
                serializer =LikeSerilizers(add_like, many=False)
                json = {
                    'message': 'successfully added !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                add_like = Like.objects.create(like=like,comment=comment, user=user)
                serializer=LikeSerilizers(add_like, many=False)
                json = {
                    'message': 'Like is created !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)
     
class  profileviwsets(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=profileSerilizers
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    @action(methods=['POST'],detail=True)
    def profile_follow(self, request, pk=None):
        if 'follow' in request.data:
            profile = Profile.objects.get(id=pk)
            follow = request.data['follow']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                add_follow= Like.objects.get(user=user.id, profile=profile.id) 
                add_follow.follow=follow
                add_follow.save()
                serializer =followSerilizers(add_follow, many=False)
                json = {
                    'message': 'successfully added !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                add_follow = Follow.objects.create(follow=follow,profile=profile, user=user)
                serializer=LikeSerilizers(add_follow, many=False)
                json = {
                    'message': 'follow is created !',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)
    @action(methods=['GET'],detail=False,url_path='search')
    def search(self,request):
        profile=Profile.objects.filter(
            first_name=request.data['first_name']
        )
        serilizers=profileSerilizers(profile,many=True)
        return Response(serilizers.data)
     
