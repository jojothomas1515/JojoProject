prof_edit_modal = document.querySelector('[data-profile-edit]')
prof_edit_close = document.querySelector('[data-modal-close]')
p_img_con = document.getElementById('img-prev')
pick_img = document.getElementById('prof-img-select')


prof_edit_modal.addEventListener('click', ()=>{
    document.querySelector("[data-modal]").style.display='block';
})
prof_edit_close.addEventListener('click' ,() =>{
        document.querySelector("[data-modal]").style.display='none';
})

pick_img.addEventListener('change',e =>{
    let fr = new FileReader()
    fr.onload = function (event){
        p_img_con.setAttribute('src',`${event.target.result}`)
    }
    fr.readAsDataURL(e.target.files[0])

})