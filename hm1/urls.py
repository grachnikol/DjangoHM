from django.urls import path, re_path
from myapp.views import main, article, users, archive, article_num, article_slug, users_id, regex, ukr_number

urlpatterns = [
    path('', main),
    path('article/', article),
    path('article/archive/', archive),
    path('article/<int:article_number>/', article_num, name='article'),
    path('article/<int:article_number>/<slug:name>/', article_slug, name='article_name'),

    path('users/', users),
    path('users/<int:user_number>/', users_id),
    re_path('^[0-9a-f]{4}\-[0-9A-z]{6}$', regex),
    re_path(r'^(0(39|67|68|96|97|98|50|66|95|99|63|73|93)\d{7})/$', ukr_number),
]
