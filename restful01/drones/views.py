from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from drones import models as drone_models
from drones import serializers as drone_serializers
from drones import drone_permission


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = drone_models.DroneCategory.objects.all()
    serializer_class = drone_serializers.DroneCategorySerializer
    name = 'dronecategory-list'

    filter_fields = (
        'name',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drone_models.DroneCategory.objects.all()
    serializer_class = drone_serializers.DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)
    queryset = drone_models.Drone.objects.all()
    serializer_class = drone_serializers.DroneSerializer
    name = 'drone-list'
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     drone_permission.IsCurrentUserOwnerOrReadOnly,
    # )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_completed',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        'manufacturing_date',
        )


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)
    queryset = drone_models.Drone.objects.all()
    serializer_class = drone_serializers.DroneSerializer
    name = 'drone-detail'
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     drone_permission.IsCurrentUserOwnerOrReadOnly,
    # )


class PilotList(generics.ListCreateAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = drone_models.Pilot.objects.all()
    serializer_class = drone_serializers.PilotSerializer
    name = 'pilot-list'
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     )
    # authentication_classes = (
    #     TokenAuthentication,
    #     )
    # permission_classes = (
    #     IsAuthenticated,
    #     )
    filter_fields = (
        'name',
        'gender',
        'races_count',
        )


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = drone_models.Pilot.objects.all()
    serializer_class = drone_serializers.PilotSerializer
    name = 'pilot-detail'
    # authentication_classes = (
    #     TokenAuthentication,
    # )
    # permission_classes = (
    #     IsAuthenticated,
    # )


class CompetitionFilter(FilterSet):
    from_achievement_date = DateTimeFilter(
        name='distance_achievement_date',
        lookup_expr='gte'
    )
    to_achievement_date = DateTimeFilter(
        name='distance_achievement_date',
        lookup_expr='lte'
    )
    min_distance_in_feet = NumberFilter(
        name='distance_in_feet',
        lookup_expr='gte'
    )
    max_distance_in_feet = NumberFilter(
        name='distance_in_feet',
        lookup_expr='lte'
    )
    drone_name = AllValuesFilter(
        name='drone__name'
    )
    pilot_name = AllValuesFilter(
        name='pilot__name'
    )

    class Meta:
        model = drone_models.Competition
        fields = (
            'distance_in_feet',
            'from_achievement_date',
            'to_achievement_date',
            'min_distance_in_feet',
            'max_distance_in_feet',
            'drone_name',
            'pilot_name',
            )


class CompetitionList(generics.ListCreateAPIView):
    queryset = drone_models.Competition.objects.all()
    serializer_class = drone_serializers.PilotCompetitionSerializer
    name = 'competition-list'
    filter_class = 'CompetitionFilter'
    ordering_fields = (
        'distance_in_feet',
        'distance_achievement_date',
        )


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drone_models.Competition.objects.all()
    serializer_class = drone_serializers.PilotCompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories':reverse(DroneCategoryList.name, request=request),
            'drone':reverse(DroneList.name, request=request),
            'pilots':reverse(PilotList.name, request=request),
            'competitions':reverse(CompetitionList.name, request=request),
        })
