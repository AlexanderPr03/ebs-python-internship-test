from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer): 

    comments = serializers.SerializerMethodField('comment_list')

    def comment_list(self,obj):
        comments = obj.comment_set.all()
        return CommentTextSerializer(comments,many=True).data

    class Meta:
        model = Blog
        fields = ('id','title','slug','body','posted','enabled','category','comments')
    


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','blog_id','text')
    
class CommentTextSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ('id','text')