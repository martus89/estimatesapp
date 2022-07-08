var updateBtns = document.getElementsByClassName('add-row')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var serviceId = this.dataset.service
		var action = this.dataset.action
		console.log('serviceId:', serviceId, 'Action:', action)

	})
}

	console.log('USER:', user)
	if (user == 'AnonymousUser'){
		console.log('User is not authenticated')

	}else{
		console.log('User is authenticated, sending data...')
	}
