import {initializeApp} from "https://www.gstatic.com/firebasejs/9.8.2/firebase-app.js";
import {
    getDownloadURL,
    getStorage,
    ref,
    uploadBytes
} from 'https://www.gstatic.com/firebasejs/9.8.2/firebase-storage.js'

tinyMCE.init({
    mode: "textareas",
    plugins: "fullscreen image",
    toolbar2: 'fullscreen image',
    toolbar1: ' bold    italic    underline    strikethrough    justifyleft    justifycenter    justifyright   justifyfull    bullist    numlist    outdent    indent    cut    copy    paste    undo    redo    link    unlink    image    cleanup    help    code    hr    removeformat    formatselect    fontselect    fontsizeselect    styleselect    sub    sup   forecolor    backcolor    forecolorpicker    backcolorpicker    charmap    visualaid    anchor   newdocument    blockquote   separator',
    height: "600px",
    width: "600px",

    images_upload_handler: (blobInfo, success, failure) => {
        upload_image(blobInfo, success, failure)
    }
});


// https://firebase.google.com/docs/web/setup#available-libraries


const firebaseConfig = {

    apiKey: "AIzaSyACnLRz2EmPraAFfi-iq2hopnzg9FoF74g",

    authDomain: "djangoblog-fb9c4.firebaseapp.com",

    projectId: "djangoblog-fb9c4",

    storageBucket: "djangoblog-fb9c4.appspot.com",

    messagingSenderId: "109437689292",

    appId: "1:109437689292:web:d40699b139d1062a3e1169"

};


const firebaseApp = initializeApp(firebaseConfig);

function upload_image(blobFile, success, failure) {
    const metadata = {
        contentType: 'image/jpeg'
    };

    const storage = getStorage(firebaseApp);
    const storageRef = ref(storage);
    const imageRef = ref(storageRef, 'images')
    const thisRef = ref(imageRef, blobFile.filename())
    uploadBytes(thisRef, blobFile.blob(), metadata).then((snapshot) => {

        getDownloadURL(thisRef).then(url => success(url))

    }).catch(e => {
        console.log(e);
        failure('failed')
    })

}







