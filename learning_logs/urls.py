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
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to create new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to create new entry of topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit an entry of topic
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
