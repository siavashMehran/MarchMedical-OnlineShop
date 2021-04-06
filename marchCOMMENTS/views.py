
from django.shortcuts import redirect, render
from .models import Comment
# Create your views here.

from django.http import JsonResponse


def like_comment(request, commentId):

    if not request.user.is_authenticated:
        return JsonResponse({"likes" : 'ابتدا وارد شوید '}, status=400) 
 

    comment_instance = Comment.objects.get(pk=commentId)
    user_liked_comments = request.user.comment_set
    

    if comment_instance not in user_liked_comments.all():
        comment_instance.likes += 1
        user_liked_comments.add(comment_instance)
        comment_instance.save()

    else:
        comment_instance.likes -= 1
        user_liked_comments.remove(comment_instance)
        comment_instance.save()



    if request.is_ajax():
        return JsonResponse({"likes" : comment_instance.likes}, status=200)

    if not request.META.get('HTTP_REFERER'):
        return redirect('/')
    else :
        return redirect(request.META.get('HTTP_REFERER'))