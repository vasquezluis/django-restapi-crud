# para llamar un modulo especial de rest framework
from rest_framework import serializers
# basado en el modelo de project
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'title', 'description', 'technology', 'created_at')
    read_only_fields = ('created_at', )
