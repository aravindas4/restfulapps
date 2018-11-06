from rest_framework import serializers
from toys import models as toys_models


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = toys_models.Toy
        fields = ('id',
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_included_in_home')
