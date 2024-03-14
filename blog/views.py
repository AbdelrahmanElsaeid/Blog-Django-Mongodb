from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import  Post
from .serializers import  PostSerializer
from accounts.models import User
from rest_framework.response import Response

#List All Published posts

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 



#Publish and Update and Delete post by specific user as Author
        
class PublishPostView(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(author=request.user)
        serializer = self.serializer_class(posts, many=True)
        return Response({'status': 'Success', 'data': serializer.data})


    def post(self,request,*args,**kwargs):
        payload=request.data 
        user_id=payload['user_id']
        title=payload['title']
        content=payload['content']
        user = User.objects.get(id=int(user_id))
        post = Post.objects.create(title=title,content=content,author=user)

        serializer = self.serializer_class(post)


        return Response({'status':'post created', 'data': serializer.data})
    
    def put(self,request,post_id,*args,**kwargs):
        payload=request.data 
        title=payload['title']
        content=payload['content']
        post = Post.objects.get(id=int(post_id))

        if post.author == request.user:
            post.title = title
            post.content = content
            post.save()

            serializer = self.serializer_class(post)
            
            return Response({'status': 'Updated', 'message': 'Updated successfully', 'data': serializer.data})
        else:
            return Response({'status': 'Unauthorized', 'message': 'You are not authorized to update this post'}, status=403)




    def delete(self,request,post_id,*args,**kwargs):
        
        
        post = Post.objects.get(id=int(post_id))
        
        if post.author == request.user:
            post.delete()
            return Response({'status': 'Deleted', 'message': 'Post deleted successfully'})
        else:
            return Response({'status': 'Unauthorized', 'message': 'You are not authorized to delete this post'}, status=403)
    










    