# jojo's Page

i picked the name because i don't have a better name in mind

## Things to do before deploy

since i dont have a static file storage and firebase is giving me issue with serving static files , i switched to
whitenoise , i'm not so certain it's working perfectly and it's subject to change later.
change the seeting as you see fit , if you've got a staticfile cloud storage do well to set it

>>heroku config:set DISABLE_COLLECTSTATIC=1

use that command to stop collectstatic from running. since this is app is not going into production it's okay 

Thank you jetbrains