from rest_framework import serializers
from .models import Task, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name', 'owner']
        read_only_fields = ['owner']


class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)
    label_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Label.objects.all(), write_only=True, source='labels'
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'owner', 'labels', 'label_ids']
        read_only_fields = ['owner']

