from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('movie_list', views.index, name='index'),
    path('<int:page>', views.index_, name='index_'),
    path('index_j', views.index_j, name='index_j'),
    path('actor_list', views.actor_list, name='actor_list'),
    path('actor_list<int:page>', views.actor_list_, name='index_'),
    path('actor_list_j', views.actor_list_j, name='index_j'),
    path('movie<str:my_id>', views.movie, name='movie'),
    path('actor<str:my_id>', views.actor, name='actor'),
    path('search', views.search, name='search'),
    path('s_m<int:page>', views.s_m_, name='s_m_'),
    path('s_m_j', views.s_m_j, name='s_m_j'),
    path('s_a<int:page>', views.s_a_, name='s_a_'),
    path('s_a_j', views.s_a_j, name='s_a_j'),
    path('s_c<int:page>', views.s_c_, name='s_c_'),
    path('s_c_j', views.s_c_j, name='s_c_j'),
]
