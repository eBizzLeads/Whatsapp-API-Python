def create_group(member, group_name, ins, api):
    url = "https://app.wapify.net/api/create-group.php"
    data = {
        "member": member,
        "group_name": group_name,
        "instance": ins,
        "apikey": api
    }

    response = requests.post(url, data=data, verify=False)
    return response.text

member = "91xxxxxxxx,91xxxxxxx,91xxxxxxx"
group_name = "My Group"
ins = "Your Instance Key"
api = "Your API Key"
print(create_group(member, group_name, ins, api))
