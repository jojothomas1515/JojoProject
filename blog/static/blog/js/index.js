const opt_icon = document.querySelectorAll('.opt-icon')
const option = document.querySelectorAll('.option')
const delete_post_button = document.querySelector("#delete-post")

opt_icon.forEach(opt => {
    opt.addEventListener('click', () => {
        if (opt.nextElementSibling.style.display === 'block') opt.nextElementSibling.style.display = "none"
        else opt.nextElementSibling.style.display = 'block'

    })
})
// opt_icon.addEventListener('mouseleave', e=>{
//         opt_icon.classList.remove('fa-close')
//
// })


document.addEventListener('click', e => {
    if (e.target.classList.contains('option-items') || e.target.classList.contains('opt-icon') || e.target.classList.contains('option'))
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
    const mv = document.cookie.split(";").filter((value, index) => {
        return value.match('(csrftoken)+.*')
    });
    const result = mv.toString().split('=').pop()
    return result
}
