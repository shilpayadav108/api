from rest_framework import serializers
from blog.models import BlogPost

classBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title','body','image','date_updated']
