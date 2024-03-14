
from accounts.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Post
from rest_framework import status
from rest_framework.authtoken.models import Token





class PublishPostViewTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser',email='testuser@gmail.com', password='password')
        self.client.login(email=self.user.email, password="password")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_publish_post(self):
        data={
            'title': "django",
            'content':"test",
            'user_id':self.user.id,

        }    

        response = self.client.post(reverse('create_post'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(),1)
        self.assertEqual(Post.objects.get().title, 'django')

        response_data = response.json()
        self.assertEqual(response_data['status'], 'post created')

        self.assertIn('title', response_data['data'])
        self.assertIn('content', response_data['data'])
        self.assertEqual(response_data['data']['title'], data['title'])
        self.assertEqual(response_data['data']['content'], data['content'])

    def test_publish_post_unauth(self):
        data={
            'title': "django",
            'content':"test",
            'user_id':self.user.id,

        }    
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('create_post'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        



    def test_get_posts(self):        
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data['status'], 'Success') 


    def test_update_post(self):
        post = Post.objects.create(title="Original Title", content="Original Content", author=self.user)
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content'
        }

        response = self.client.put(reverse('update_post', kwargs={'post_id': post.id}), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'Updated Title')
        response_data = response.json()
        self.assertEqual(response_data['status'], 'Updated')
        self.assertEqual(response_data['message'], 'Updated successfully') 



    def test_delete_post(self):
        post = Post.objects.create(title="Original Title", content="Original Content", author=self.user)
        response = self.client.delete(reverse('update_post', kwargs={'post_id': post.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['status'], 'Deleted')
        self.assertEqual(response_data['message'], 'Post deleted successfully')
          

