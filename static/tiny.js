tinyMCE.init({
    mode: "textareas",
    plugins: "fullscreen image",
    toolbar2: 'fullscreen image',
    toolbar1: ' bold    italic    underline    strikethrough    justifyleft    justifycenter    justifyright   justifyfull    bullist    numlist    outdent    indent    cut    copy    paste    undo    redo    link    unlink    image    cleanup    help    code    hr    removeformat    formatselect    fontselect    fontsizeselect    styleselect    sub    sup   forecolor    backcolor    forecolorpicker    backcolorpicker    charmap    visualaid    anchor   newdocument    blockquote   separator',
    height: "600px",
    width: "600px",

    images_upload_handler: (blobInfo, success, failure) => {
        const formData = new FormData()
        formData.append('image', blobInfo.blob(), blobInfo.filename());
        console.log(blobInfo.blob())
        fetch(/upload/, {
            method: 'POST', body: formData, headers: {'X-CSRFToken': document.cookie.split('=')[1]}
        }).then(res => res => {
            if (res.ok) {
                success(res.data)
            }
        }).catch(failure('try again'))
    }
});

