from flask import Flask, url_for, Response, request, make_response

app = Flask(__name__)

import plivo
import random
import os

@app.route('/', methods=['POST', 'GET'])
def index():
    r = plivo.Response()
    r.addSpeak("hello customer, how are you")
    response = make_response(r.to_xml())
    response.headers['Content-Type'] = 'text/xml'
    return response


@app.route('/DIDCallForwarding/',methods=['GET','POST'])
def did_call_forwarding():
    print "\n========DID Call Forwarding app in use=====>"
    print "request values are====>",request.values.items()," got values?"
    if request.method == "GET":
        print "inside GET Method"
        number = request.args.get('Number', None)
        print number
        user = request.args.get('User',None)
        print user
    else:
        print "inside POST method====>"
        number = request.form.get('Number','')
        user = request.form.get('User','')
    if number:
        callto = number
    else:
        callto = user
    r = plivo.Response()
    params = {'action' : 'http://nameless-inlet-6252.herokuapp.com/action/'}
    dial = r.addDial(**params)
    body = callto
    if number:
        dial.addNumber(body)
    else:
        dial.addUser(body)
    response = make_response(r.to_xml())
    response.headers['Content-Type'] = 'text/xml'
    return response
    return("0") 

'''
app for checking whether call is being recieved ar not
if call is not recieved then it will ask caller to leave a voice message
'''
@app.route('/action/', methods=['GET', 'POST'])
def action_url():
    print "\n=========== action_url ======="
    response_action_url = request.form.items();
    print '\nresponse_action_url ===>>> ', response_action_url
    dialstatus = request.form.get('DialStatus','')
    print "dial status is:",dialstatus 
    if dialstatus == "completed":
        print "diastaus completed"
    else: 
        print "dial status not completed."
        r = plivo.Response() 
        body = 'user is unable to answer, please leave a message after a beep and press # after message.'
        r.addSpeak(body)
        params = {
                'action' : 'http://nameless-inlet-6252.herokuapp.com/recordaction/',
                'playBeep' : 'true',
                'finishOnKey' : '#' }
        r.addRecord(**params)
        response = make_response(r.to_xml())
        response.headers['Content-Type'] = 'text/xml'
        return response
    return 'action_url'

'''
voice message is recorded here
and a link to record is sent to DID_number
'''

@app.route('/recordaction/',methods=['GET','POST'])
def record_action_url():
    print "\n=======voice message record action url=============>"
    record_action = request.form.items();
    print record_action
    From = request.form.get('From','')
    to = request.form.get('To','')
    recordurl = request.form.get('RecordUrl','')
    print "from",From
    print "to",to
    print "recordurl",recordurl
    print "\n==========voicemessage sending action taking place=====>"
    r = plivo.Response()
    body = recordurl
    params = {
        'src' : to,
        'dst' : From
        }
    r.addMessage(body, **params)
    response = make_response(r.to_xml())
    response.headers['Content-Type'] = 'text/xml'
    return response
    return("0")


'''
message sent to DID_number is forwarded to a number
which is given in message_url in app
'''
@app.route('/message/',methods=['GET','POST'])
def message_detail():
    print "\n=========message forwarding details======>"
    print "request values message url are====>",request.values.items()," got values?"
    if request.method == "GET":
        print "inside message GET Method"
        number = request.args.get('Number', None)
        print number
        to = request.args.get('To', None)
        From = request.args.get('From', None)
        text = request.args.get('Text', None)
        type = request.args.get('Type', None)
    else:
        print "inside POST method====>"
        number = request.form.get('Number','')
        print number
        to = request.form.get('To', None)
        From = request.form.get('From', None)
        text = request.form.get('Text', None)
        type = request.form.get('Type', None)

    r = plivo.Response()
    body = text
    params = {
        'src' : From,
        'dst' : number
        }
    r.addMessage(body, **params)
    response = make_response(r.to_xml())
    response.headers['Content-Type'] = 'text/xml'
    return response
    return("0")




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
