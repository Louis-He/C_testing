from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercise/<int:exercise_id>', views.exercise, name='exercise'),
    path('input/input_<int:exercise_id>.in', views.input, name='input'),
    path('skeleton/<int:exercise_id>/<str:platform>',
         views.skeleton, name='skeleton'),
    path('syllabus', views.syllabus, name='syllabus'),
    path('cookbook_<str:section>',
         views.cookbook_index, name='cookbook_index'),
]
