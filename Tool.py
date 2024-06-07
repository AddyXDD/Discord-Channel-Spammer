import requests

payload  = {
    'content': "testing py"
}
#to get authorization press ctrl shift + I and go to network and send a message, click the @message that pops up and scroll down to the request headers and copy the authorization.
header = {
    'authorization': 'authorization-token'
#to get channel api follow the same steps as above but at the general tab and copy the request url and paste here
}
for i in range (10):
    r = requests.post('enter-channel-request-api', data=payload,  headers=header)
