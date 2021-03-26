# from django.contrib.auth.models import User, Group
from blog.models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  #['author', 'body', 'created_on', 'post']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False, allow_null=True )
    class Meta:
        model = Post
        fields = ['title', 'body', 'created_on', 'last_modified', 'author', 'comments']


    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        if 'comments' in validated_data:
            comments_data = validated_data.pop('comments')

            for comment_data in comments_data:
                comment = Comment.objects.create(post=post, **comment_data)

        return post
