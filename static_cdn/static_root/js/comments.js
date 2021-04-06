
let likeBtn = document.querySelectorAll('.like-btn') ;

likeBtn.forEach(function(e, key, parent){
    e.addEventListener('click', function(){
        let commentId = e.id.replace('like-btn-', '') ; 

        $.ajax({
            type : 'post', 
            url : 'localhost:8000/comment/like/',
            data : { 'commentId' : commentId } ,
            succsess : function(response){
                console.log('success');
                console.log(response);
            } , 
            error : function(response){
                console.log('error');
                console.log(response);
                
            },

        }) ;

    });
});






/* 

{% url 'increment_likes' comment.id %}

*/