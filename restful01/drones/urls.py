from django.urls import path, include
from drones import views as drone_views

urlpatterns = [
    path('', drone_views.ApiRoot.as_view(), name=drone_views.ApiRoot.name),
    path('drone-categories/', drone_views.DroneCategoryList.as_view(), name=drone_views.DroneCategoryList.name),
    path('drone-categories/<int:pk>/', drone_views.DroneCategoryDetail.as_view(), name=drone_views.DroneCategoryDetail.name),
    path('drones/', drone_views.DroneList.as_view(), name=drone_views.DroneList.name),
    path('drones/<int:pk>/', drone_views.DroneDetail.as_view(), name=drone_views.DroneDetail.name),
    path('pilots/', drone_views.PilotList.as_view(), name=drone_views.PilotList.name),
    path('pilots/<int:pk>/', drone_views.PilotDetail.as_view(), name=drone_views.PilotDetail.name),
    path('competitions/', drone_views.CompetitionList.as_view(), name=drone_views.CompetitionList.name),
    path('competitions/<int:pk>/', drone_views.CompetitionDetail.as_view(), name=drone_views.CompetitionDetail.name)
]