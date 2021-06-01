$(document).ready(function(){


    let likeBtn = document.querySelectorAll('.like-btn') ;
    const csrf = document.getElementsByName('csrfmiddlewaretoken')

    likeBtn.forEach(function(e, key, parent){

        e.addEventListener('click', function(){

            let commentId = e.id.replace('like-btn-', '') ; 
            var adress = '/comment/like/'+commentId
            
            $.ajax({
                type : 'get', 
                url : adress,
                data : {'csrfmiddlewaretoken' : csrf[0].value} ,
                enctype: 'json',

                success : function(r){ 
                    console.log(r.likes);
                    const likeSpan = e.childNodes[0].childNodes[0].childNodes[0] ;
                    likeSpan.innerHTML = r.likes
                    e.childNodes[0].childNodes[0].style = 'color : #22fd22;'
                    
                    
                 },
                 
                error : function(){
                    alert('ابتدا وارد شوید')
                }
            }) ;

        });
    });






    /* 

    {% url 'increment_likes' comment.id %}

    */
})