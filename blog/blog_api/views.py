from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Contact
from .serializers import PostSerializer, ContactSerializer

class ArticleListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the articles for given requested user
        '''
        articles = Post.objects.all()
        serializer = PostSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Article with given data
        '''
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'author': request.data.get('author'),
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailApiView(APIView):
    # add permission to check if user is authenticated

    # 1. Retrieve
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieve the Article with given pk
        '''
        article = Post.objects.get(pk=pk)
        serializer = PostSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Update
    def put(self, request, pk, *args, **kwargs):
        '''
        Update the Article with given pk and data
        '''
        article = Post.objects.get(pk=pk)
        data = {
            'title': request.data.get('title'), 
            'content': request.data.get('content'), 
            'author': request.data.get('author'),
        }
        serializer = PostSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Delete the Article with given pk
        '''
        article = Post.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContactListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the contacts for given requested user
        '''
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Contact with given data
        '''
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
            'phone': request.data.get('phone'),
            'message': request.data.get('message'),
        }
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetailApiView(APIView):

    # 1. Retrieve
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieve the Contact with given pk
        '''
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Update
    def put(self, request, pk, *args, **kwargs):
        '''
        Update the Contact with given pk and data
        '''
        contact = Contact.objects.get(pk=pk)
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
            'phone': request.data.get('phone'),
            'message': request.data.get('message'),
        }
        serializer = ContactSerializer(contact, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Delete the Contact with given pk
        '''
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)