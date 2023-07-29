from rest_framework import serializers
from .models import Comment,Follow,Profile,Post,Like

class profileSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class LikeSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields='__all__'

class followSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'

class commentSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class postSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
