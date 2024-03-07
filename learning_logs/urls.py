"""urlpatterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with topics
    path('topics/', views.topics, name='topics'),
    # Page with additional information about a topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
