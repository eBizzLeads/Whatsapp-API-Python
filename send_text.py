import requests

def send_message(number, msg, ins, api):
    url = "https://app.wapify.net/api/text-message.php"
    data = {
        "number": number,
        "msg": msg,
        "instance": ins,
        "apikey": api
    }

    response = requests.post(url, data=data, verify=False)
    return response.text

number = "91xxxxxxxx"
msg = "Your Messages"
ins = "Your Instance Key"
api = "Your API Key"
print(send_message(number, msg, ins, api))
