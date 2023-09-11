def send_media_message(number, msg, media, ins, api):
    url = "https://app.wapify.net/api/media-message.php"
    data = {
        "number": number,
        "msg": msg,
        "media": media,
        "instance": ins,
        "apikey": api
    }

    response = requests.post(url, data=data, verify=False)
    return response.text

number = "91xxxxxxxx"
msg = "Your Messages"
media = "Media URL With HTTPS"
ins = "Your Instance Key"
api = "Your API Key"
print(send_media_message(number, msg, media, ins, api))
