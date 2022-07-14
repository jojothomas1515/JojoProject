const open_edit = document.querySelector('[data-user-edit-icon]')
const close_edit = document.querySelector('[data-user-edit-close]')
const image_image = document.querySelector('[data-input-image]')
const opt_icon = document.querySelectorAll('.opt-icon')
const option = document.querySelectorAll('.option')
const delete_post_button = document.querySelector("#delete-post")

open_edit.addEventListener('click', () => {
    const modal = document.querySelector('.modal')
    modal.style.opacity = 1;
    modal.style.pointerEvents = 'initial';

})
close_edit.addEventListener('click', () => {
    const modal = document.querySelector('.modal')
    modal.style.opacity = 0;
    modal.style.pointerEvents = 'none';
})

image_image.addEventListener('change', (e) => {
    let img = e.target.files[0]

    const fr = new FileReader()
    fr.onload = function (e) {
        document.getElementById('mi-c').src = e.target.result
    }
    fr.readAsDataURL(img)
})


opt_icon.forEach(opt => {
    opt.addEventListener('click', e => {
        if (opt.nextElementSibling.style.display === 'block') opt.nextElementSibling.style.display = "none"
        else opt.nextElementSibling.style.display = 'block'

    })
})
// opt_icon.addEventListener('mouseleave', e=>{
//         opt_icon.classList.remove('fa-close')
//
// })


document.addEventListener('click', e => {
    if (e.target.classList.contains('opt-icon') | e.target.classList.contains('option') | e.target.classList.contains('option-items')) return
    else option.forEach(opt => opt.style.display = "none")
})

delete_post_button.addEventListener('click', e => delete_post(e))
const delete_post = async e => {

    const post_id = e.target.dataset.postid
    const res = await fetch(`/deletePost/${post_id}`, {
        method: 'DELETE',
        headers: {
            "X-CSRFToken": `${getCsrfToken()}`
        }
    })
    res.status === 200 ? window.location.reload(true) : alert('delete failed')
}

function getCsrfToken() {
    const mv = document.cookie.split(";").filter((value, index) => {
        return value.match('(csrftoken)+.*')
    });
    const result = mv.toString().split('=').pop()
    return result
}


