from django.urls import path

from .views import (
    ContentListView,
    create_content,
    delete_content,
    ContentUpdateView
)

app_name = 'webapp'


urlpatterns = [
    path('', ContentListView.as_view(), name='content-list'),
    path('/create', create_content, name='create-content'),
    path('/delete', delete_content, name='delete-content'),
    path('/update/<int:pk>', ContentUpdateView.as_view(), name='update-content'),
]
