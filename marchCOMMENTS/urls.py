
from marchCOMMENTS.views import like_comment
from django.urls import path


urlpatterns = [
    path('comment/like/<int:commentId>', like_comment, name='increment_likes')
]
