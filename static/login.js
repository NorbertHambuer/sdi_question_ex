function login(user, password){
	    var bodyFormData = new FormData();
        bodyFormData.set('username', user);
        bodyFormData.set('password', password);

        axios.post('https://flask-chatbot-generator.herokuapp.com/login', bodyFormData, {withCredentials: true})
            .then(res => {
				console.log(res);
                if(res.data.user_id) {                 
                    localStorage.setItem('csrf_token', res.data.csrf_token);
                   
                }else{
                    console.log("login failed!");
                }
            });
}

function get_bot_id(){
        axios.get('https://flask-chatbot-generator.herokuapp.com/get_bot_id?bot_name=SDI_example&user_id=1', {withCredentials: true})
            .then(res => {
                console.log(res);
				localStorage.setItem('bot_id', res.data.id);
            });
}