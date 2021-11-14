
$.ajaxSetup({
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let createContent = function (e){
    e.preventDefault();
    let formData = $("#createForm").find('form').serialize()
    let targetUrl = $("#createForm").data('targeturl')
    let closeModalbtn = $("#closeCreateModal").trigger('click')


    $.ajax({
        url: targetUrl,
        type: 'post',
        data: formData,
        success: function(response) {
            console.log(response)
            location.reload()
            alert(response['message'])

        },
        failure: function(response) {
            console.log(response)
            alert('ERROR');
        }
    });
}


let deleteContent = function (e){
    e.preventDefault();
    let contentId = e.target.parentElement.id
    let targetUrl = e.target.parentElement.dataset.deleteurl
    console.log(targetUrl)

    $.ajax({
        url: targetUrl,
        type: 'post',
        data: contentId,
        success: function(response) {
            console.log(response)
            location.reload()
            alert(response['message'])

        },
        failure: function(response) {
            console.log(response)
            alert('ERROR');
        }
    });
}


let getUpdateForm = function (e){
    e.preventDefault();
    let contentId = e.target.parentElement.id
    let targetUrl = e.target.dataset.updateurl

        $.ajax({
        url: targetUrl,
        type: 'get',
        // data: '',
        success: function(response) {
            $("#openUpdateFormModel").trigger('click')
            $("#updateModalLabel").text('Update Content')
            $("#updateForm").html(response)
            $("#updateForm").append(`<button class="updateContent" hidden id="${targetUrl}"></button>`)
        },
        failure: function(response) {
            console.log(response)
            alert('ERROR');
        }
    });
}

let updateContent = function (e){
    e.preventDefault();
    let formData = $("#updateForm").serialize()
    let targetUrl = $("#updateForm").find('.updateContent')[0].id
    $("#closeUpdateModal").trigger('click')


    $.ajax({
        url: targetUrl,
        type: 'post',
        data: formData,
        success: function(response) {
            location.reload()
            alert(response['message'])

        },
        failure: function(response) {
            console.log(response)
            alert('ERROR');
        }
    });
}