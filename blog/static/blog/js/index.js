const opt_icon = document.querySelectorAll('.opt-icon')
const option = document.querySelectorAll('.option')
const delete_post_button = document.querySelector("#delete-post")
const edit_post_button = document.querySelector("#edit-post")

opt_icon.forEach(opt => {
    opt.addEventListener('click', () => {
        if (opt.nextElementSibling.style.display === 'flex') opt.nextElementSibling.style.display = "none"
        else opt.nextElementSibling.style.display = 'flex'

    })
})
// opt_icon.addEventListener('mouseleave', e=>{
//         opt_icon.classList.remove('fa-close')
//
// })


document.addEventListener('click', e => {
    if (e.target.classList.contains('option-items') || e.target.classList.contains('opt-icon') || e.target.classList.contains('option')) return null
    else option.forEach(opt => opt.style.display = "none")
})

delete_post_button.addEventListener('click', e => delete_post(e))
const delete_post = async e => {

    const post_id = e.target.dataset.postid
    const res = await fetch(`/deletePost/${post_id}`, {
        method: 'DELETE', headers: {
            "X-CSRFToken": `${getCsrfToken()}`
        }
    })
    res.status === 200 ? window.location.reload(true) : alert('delete failed')
}

function getCsrfToken() {
    const mv = document.cookie.split(";").filter((value) => {
        return value.match('(csrftoken)+.*')
    });
    return mv.toString().split('=').pop()
}

edit_post_button.addEventListener("click", e=>edit_post(e))

const edit_post = async e => {

    const post_id = e.target.dataset.postid
    window.location.replace(`/editpost/${post_id}`)
}

