const open_edit = document.querySelector('[data-user-edit-icon]')
const close_edit = document.querySelector('[data-user-edit-close]')

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