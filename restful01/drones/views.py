from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from drones import models as drone_models
from drones import serializers as drone_serializers


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = drone_models.DroneCategory.objects.all()
    serializer_class = drone_serializers.DroneCategorySerializer
    name = 'dronecategory-list'


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drone_models.DroneCategory.objects.all()
    serializer_class = drone_serializers.DroneCategorySerializer
    name = 'dronecategory-detail'


class DroneList(generics.ListCreateAPIView):
    queryset = drone_models.Drone.objects.all()
    serializer_class = drone_serializers.DroneSerializer
    name = 'drone-list'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drone_models.Drone.objects.all()
    serializer_class = drone_serializers.DroneSerializer
    name = 'drone-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = drone_models.Pilot.objects.all()
    serializer_class = drone_serializers.PilotSerializer
    name = 'pilot-list'


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = drone_models.Pilot.objects.all()
    serializer_class = drone_serializers.PilotSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = drone_models.Competition.objects.all()
    serializer_class = drone_serializers.PilotCompetitionSerializer
    name = 'competition-list'


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
