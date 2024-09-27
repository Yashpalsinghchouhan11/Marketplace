document.getElementById('signup-form').addEventListener('click', function(event){
    event.preventDefault();
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    formdata = new FormData(document.getElementById('signup-form'));

    const jsonobject = {}

    formdata.forEach(function(value, key){
        jsonobject[key] = value
    });
    const csrfToken = getCookie('csrftoken');

    const jsondata = JSON.stringify(jsonobject);

    fetch('/singup/',
    {
        method: 'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrfToken
        },
        body: jsondata
    })

    .then((response) =>response.json())
    .then(data=>{
            console.log('success',data)
        })
    }).catch((err) => {
        console.log('error',err)
    });