const open_edit = document.querySelector('[data-user-edit-icon]')
const close_edit = document.querySelector('[data-user-edit-close]')
const image_image = document.querySelector('[data-input-image]')

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

image_image.addEventListener('change', (e)=>{
    let img = e.target.files[0]

    const fr = new FileReader()
    fr.onload =function (e){
        document.getElementById('mi-c').src=e.target.result
    }
    fr.readAsDataURL(img)
})




