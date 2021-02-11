from django.urls import path
from . import views  # using the relative import statement to import views

# url configuration
# movies/1
# /old_system/movies/1

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),  # root of this apps
    path('<int:movie_id>', views.detail, name='detail')
]
