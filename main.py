import requests
import json


import login, utils

headers = {
    "OS": "android",
    "OS-Version": "25",
    "Manufacturer": "samsung",
    "Model": "SM-G955N",
    "Resolution": "1080x1920",
    "Market": "xiaomi",
    "ApplicationId": "app.podcast.cosmos",
    "App-Version": "2.50.1",
    "App-BuildNo": "836",
    "x-jike-device-id": "f9783655-e94f-4113-a5e7-95981cd3b190",
    "App-Permissions": "100100",
    "abtest-info": "{}",
    "WifiConnected": "true",
    "x-jike-access-token": "",
    "x-jike-refresh-token": "",
    "Content-Type": "application/json;charset=utf-8",
    "Content-Length": "41",
    "Host": "api.xiaoyuzhoufm.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.2",
    "x-jike-device-properties": '{"uuid":"3b925051-9143-4548-afd4-27e1d32a189f","android_id":"6066ef25337fa198","oaid":"","vaid":"","aaid":""}',
    "sentry-trace": "00000000000000000000000000000000-0000000000000000-0",
}


#url = "https://api.xiaoyuzhoufm.com/v1/category/podcast/list-tabs"

phone = "123456"   # 手机账号


def setToken():
    if utils.tokenExist():
        access_token = utils.getToken()
        headers['x-jike-access-token'] = access_token
        # if ping():
        return access_token
    return resetToken()


def resetToken():
    login.sendCode(phone)
    code = input("输入你收到的code:")
    myToken, _ = login.getToken(login.login(phone, code))
    utils.saveToken(myToken)
    headers['x-jike-access-token'] = myToken
    return myToken


def ping():
    print("ping status")
    url = "https://api.xiaoyuzhoufm.com/v1/user-config/get"
    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    return resp.status_code == 200


def getListByTab(id):
    url = "https://api.xiaoyuzhoufm.com/v1/category/podcast/list-by-tab"
    data = {"categoryId": id, "tab": "ALL", "omitSubscribed": False, "loadMoreKey": 10.0}
    # data = {"categoryId": "63c76a8924b1622727bd321b"}
    resp = requests.post(url, json.dumps(data), headers=headers)
    tabMap = json.loads(resp.text)
    resMap = {}
    for item in tabMap['data']:
        pod = item['podcast']
        resMap[pod['brief']] = pod['pid']
    print(resMap)
    return resMap


def getCategoryList():
    url = "https://api.xiaoyuzhoufm.com/v1/category/list-all"
    resp = requests.post(url, "{}", headers=headers)
    if resp.status_code == 401:
        resetToken()
    categoryMap = json.loads(resp.text)
    resMap = {}
    for item in categoryMap['data']:
        resMap[item['name']] = item['id']
    print(resMap)
    return resMap


if __name__ == "__main__":
    token = setToken()
    cl_map = getCategoryList()
    while True:
        title = input("输入你想爬取的内容:")
        tid = cl_map.get(title)
        if tid is None:
            print("not find")
            continue
        getListByTab(tid)
        break



