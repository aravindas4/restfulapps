from rest_framework import serializers

from drones import models as drone_models
from django.contrib.auth.models import User


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
                many=True,
                read_only=True,
                view_name='drone-detail',
            )

    class Meta:
        model = drone_models.DroneCategory
        fields = (
                    'url',
                    'id',
                    'name',
                    'drones'
        )


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
                                queryset=drone_models.DroneCategory.objects.all(),
                                slug_field='name'
                    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = drone_models.Drone
        fields = (
                    'url',
                    'name',
                    'drone_category',
                    'owner',
                    'manufacturing_date',
                    'has_it_completed',
                    'inserted_timestamp'
        )


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = drone_models.Competition
        fields = ('url', 'id', 'distance_in_feet', 'distance_achievement_date', 'drone')


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=drone_models.Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = drone_models.Pilot
        fields = (
                'url',
                'name',
                'gender',
                'gender_description',
                'races_count',
                'inserted_timestamp',
                'competitions'
        )
        depth = 1


class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(queryset=drone_models.Pilot.objects.all(), slug_field='name')
    drone = serializers.SlugRelatedField(queryset=drone_models.Drone.objects.all(), slug_field='name')

    class Meta:
        model = drone_models.Competition
        fields = (
                    'url',
                    'pk',
                    'distance_in_feet',
                    'distance_achievement_date',
                    'pilot',
                    'drone'
        )


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = drone_models.Drone
        fields = (
                    'url',
                    'name',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
                many=True,
                read_only=True,
    )

    class Meta:
        model = User
        fields = (
                    'url',
                    'pk',
                    'username',
                    'drone',
        )


