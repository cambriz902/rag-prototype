from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/course-assistant/', include('course_assistant.urls'))
]
