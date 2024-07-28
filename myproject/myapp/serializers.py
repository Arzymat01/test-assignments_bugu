from rest_framework import serializers
from .models import CustomUser, Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'is_author', 'is_subscriber')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            is_author=validated_data.get('is_author', False),
            is_subscriber=validated_data.get('is_subscriber', True)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'is_public', 'author')
        read_only_fields = ('author',)
