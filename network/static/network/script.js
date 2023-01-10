addEventListener('DOMContentLoaded', (event) => {
    

    
    document.addEventListener('click', function(e){   

        if(e.target.className === 'btn btn-primary edit'){
            // go to edit form 
            var post = document.getElementById('post-'+e.target.id);
            var edit = document.getElementById('edit-'+e.target.id);
            post.style.display='none';
            edit.style.display='block';
        
        }

        if(e.target.className === 'btn btn-danger edit'){
            // discard edits
            var post = document.getElementById('post-'+e.target.id);
            var edit = document.getElementById('edit-'+e.target.id);
            post.style.display='block';
            edit.style.display='none';
        
        }

        if(e.target.className === 'btn btn-success edit'){
            // save edits
            var post = document.getElementById('post-'+e.target.id);
            var edit = document.getElementById('edit-'+e.target.id);

            // get csrf and textarea content from page
            let csrftoken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
            var textarea = document.getElementById('textarea-'+e.target.id).value;

            // send data to edit view and get response and change the content in post
            fetch('/edit/'+e.target.id,{
                method:'POST',
                headers:{
                    "Content-type":"application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({
                    content: textarea
                })
            })
            .then(response => response.json())
            .then(result=>
                document.getElementById('content-'+e.target.id).innerHTML=result["data"]  
            )

            // show post and hide edit form
            post.style.display='block';
            edit.style.display='none';
        }



    })
});
