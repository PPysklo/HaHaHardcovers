const addBtns = document.getElementsByClassName('addItem')


for (var i = 0; i < addBtns.length ; i++  ){
    addBtns[i].addEventListener('click', function(){
        console.log("dasd")
        var bookId = this.dataset.book
        var action = this.dataset.action

        if(user === 'AnonymousUser'){
            console.log("User is not authenticated")
        }
        else{
            updateUserOrder(bookId,action)
        }
    })
}

function updateUserOrder(bookId, action){


		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'bookId':bookId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}


