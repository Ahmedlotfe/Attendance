from django.urls import path
from . import views, api

urlpatterns = [
    path('check_in/', views.check_in, name='check_in'),         # /attendance/check_in/
    path('check_out/', views.check_out, name='check_out'),      # /attendance/check_out/
    path('dashboard/', views.dashboard, name='dashboard'),      # /attendance/dashboard/

    # API
    path('api/attendances/', api.AttendanceListCreateAPIView.as_view()),                # List and create
    path('api/attendances/<int:pk>/', api.AttendanceDetailAPIView.as_view()),           # Retrieve
    path('api/attendances/<int:pk>/update/', api.AttendanceUpdateAPIView.as_view()),    # Update
    path('api/attendances/<int:pk>/delete/', api.AttendanceDeleteAPIView.as_view()),    # Delete
]
