/*import data from './comments.json'*/

function publicar_comentario(){
    let commentary_text = document.getElementById('commentary-input').value;
    let name_text = document.getElementById('name-input').value;

    if (commentary_text != '' && name_text != ''){
        document.getElementById('commentaries').innerHTML += '<div class="commentary-container">'
        + '\n<p class="commentary-author">'+name_text+'</p>'
        + '\n<p class="commentary-text">'+commentary_text+'</p>'
        + '\n<p class="commentary-qualification"><b>4.5</b>/5</p>'
        + '\n</div>';    
    }
    
}


/*function loadCommentaries(){
    alert(data);
}*/