from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer, CommentTextSerializer

from drf_util.decorators import serialize_decorator

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        return Response(BlogSerializer(blog).data)

class BlogItemCreate(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            posted='posted',
            enabled=validated_data['enabled'],
            category=validated_data['category']
        )

        blog.save()

        return Response(BlogSerializer(blog).data) 

class CommentItemView(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        comment = get_object_or_404(Comment.objects.filter(pk=pk))

        return Response(CommentSerializer(comment).data)

class CommentListView(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        comments = Comment.objects.filter(blog_id=pk)

        return Response({"results":CommentSerializer(comments, many=True).data})


class CommentItemCreate(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comment.objects.create(
            blog_id=validated_data['blog_id'],
            text=validated_data['text'],
        )

        comment.save()

        return Response(CommentSerializer(comment).data) 