from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = "feedback_site:user-detail")

    class Meta:
        model = Feedback
        fields = ('url','title','description','creator')