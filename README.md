Voicemail using Plivo XML
-------------------
A callforward application - Incoming call on Plivo DID will get forwarded to SIP Endpoint, Mobile and WebRTC.
If the Dial fails then it should go to some voicemail application. 


==================================================================
INSTALLATION INSTRUCTIONS
==================================================================

visit for more detail to  see, how to deploy a flask app in heroku:
 https://devcenter.heroku.com/articles/python
 https://github.com/zachwill/flask_heroku


Instructions to install this app:
heroku login
1. $git clone git@github.com:zachwill/flask_heroku.git
2. $cd flask_heroku
3. $virtualenv venv --distribute
4. $source venv/bin/activate
5. $pip install Flask gunicorn
6. 4pip install -r requirements.txt
7. $foreman start


   Make sure things are working properly curl or a web browser, then Ctrl-C to exit.

8. $Now Deployment part:
9, $git init
10. $git add .
11. $git commit -m "init"
12. $heroku create
13. $git push heroku master
14. $heroku ps:scale web=1
15. $heroku ps
16. $heroku open


===================================================================
USING INSTRUCTIONS
===================================================================

1. Find the url of your new created app
2. Create  an app at www.plivo.com/app/, inside your account
   Application name : {name of your app}
   Answer url :
              url_of_app/DIDCallForwarding/?Number={the number to which call to be forwarded}   or
              url_of_app/DIDCallForwarding/?User={the end point user name}
                   Example:
                   http://nameless-inlet-6252.herokuapp.com/DIDCallForwarding/?Number=917829623306  or
                   http://nameless-inlet-6252.herokuapp.com/DIDCallForwarding/?User=sip:amit12345@phone.plivo.com
   Answer method: GET
   Hangup url: same as Answer url
   Hangup method : GET
   Message url: url_of_app/message/?Number={you number to which voice mail to be forwarded}
	           example:  http://nameless-inlet-6252.herokuapp.com/message/?Number=14152953959
   Message method: GET



Connect this app to your Plivo_DID number. (to buy a Plivo DID number:https://manage.plivo.com/number/search/ )
 Now you can call at your plivo_DID number and call will be forwarded to your number or sip_end_point which you have given above in answer_url.
if you do not answer the call , the caller will be able to record a voice mail and the link to voice mail will be sent to your number 
which you have given in Message url, and you can go to link for listening the recorded voice.

use the following dummy link to check the working of app without installing:
----------------------------------------------------------------------------
link to website: www.plivo.com/app

Answer url and Hangup url: 
	http://nameless-inlet-6252.herokuapp.com/DIDCallForwarding/?Number={your number to which call ro be forwarded}  or
        http://nameless-inlet-6252.herokuapp.com/DIDCallForwarding/?User={your sip endpoint name}
Message url:
http://nameless-inlet-6252.herokuapp.com/message/?Number={you number to which voice mail to be forwarded}                   



