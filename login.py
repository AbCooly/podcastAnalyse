import json
import requests

headers = {
    'OS': 'android',
    'OS-Version': '25',
    'Manufacturer': 'samsung',
    'Model': 'SM-G955N',
    'Resolution': '1080x1920',
    'Market': 'xiaomi',
    'ApplicationId': 'app.podcast.cosmos',
    'App-Version': '2.50.1',
    'App-BuildNo': '836',
    'x-jike-device-id': '6d460fb1-40c8-4be6-bac0-71ada85f271d',
    'App-Permissions': '100100',
    'WifiConnected': 'true',
    'Content-Type': 'application/json;charset=utf-8',
    'Content-Length': '72',
    'Host': 'api.xiaoyuzhoufm.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.2',
    'x-jike-device-properties': '{"uuid":"b7686eb8-a596-4e95-b577-ba9ef07a5212","android_id":"6066ef25337fa198","oaid":"","vaid":"","aaid":""}',
    'sentry-trace': '00000000000000000000000000000000-0000000000000000-0',
}


# {"tab": "648c21dd7671f32ba435d382"}

headers = {


'abtest-info': '{}',
'WifiConnected': 'true',
'x-jike-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiWU95SWZhVWphQlZqVFc4azVUdXZOeVwvRzR3b3hHT3h4aGJraHMrXC8zSEZLNG9Ra0l1SUdPTlUxY01BeXJcL1o0QnpxN3JTXC9heFM4UEpMRTkxRFh0ZXdxVXlcLzdtaVE4QXVBcHdGbm5POG1qOFN2VzZ1Z1BQZjdERnhMQkVjbFoyRHpaZ0lcL0JvTmthdjFBTVY3a3VJbG16WllpbWc1a3oxbDhVM0YxYXNVM1pNc0JhS0tFRStyXC84OFwvMDVtME1CV1Z3MmNUeVpvOWFqeklzYkpGZzFsQXNMRStVZitFT1pwN1pkemNvQ3JpRnpYK3FlOXVkeWRmb1pzdHc4MEllY0czZ2lUUDU1NXhrU1JQZVZkM3RoOGhicFNuZzc5OGtaVkh2XC9CVWVUcUFQOVlJYzZjRFZIUjZHVGFKU3BjSHRTT2F4YVNWbWE3YU5PTzNQbzRPTVwvOXAxTlNTMzUwYndLa0pzY1dsTnM1TGJUT3RqM1ZlblZOMHR0K0FsS05MWlRHeko0YzN2d0tQck8xS2U0NFVlVU1hcDlCSytibndscmVkTVwvakZzUEI4V2xrPSIsInYiOjMsIml2IjoiTm9UUVZwQ2RWZ1BrdE1YYkNhdzJFdz09IiwiaWF0IjoxNjg3MjYwMzQ3LjY3OX0.c0kekygveIMrbqvmNgZ3LJ1pNAA8Ou9GknfkzIFIVag',
'x-jike-refresh-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoib2J5cDdNeWJzb3RBWk94MTZZU0thalhTeGN3OE9BZnJHRVRqTEljTDJvOW93MVRZWlNKSWNGdkREQkhES0sweUZleVZpTWhMZWk4Z25qNTkyRkg5WlluUDZwOW0xdTZSZVJGNlRyQTF3U1dpQ0JDc0JNa2dqSjh2TGRcL3JPOTluQ2JLTlNDUHFNOWdtdm0ybW5heHJ1ajVWRlVMNmVFQVVcL29hd095ZXgySGFSUUVmZVpaNk1ncmhNSGl1V2NQNzBNMHpPTFFhRkNmelNYcVZmTVZiV200UTNyRHUrV01SVFVVMnZtRlwvbHFCampvZXVnNzJmVjBqVFFHcTBxSzRFUSIsInYiOjMsIml2IjoiYktoT3JGOWp3alBpSVBiYU1EdW0zUT09IiwiaWF0IjoxNjg3MjYwMzQ3LjY3OX0.y3KMty-BZNShF9Q3rjc7GDc-1O_ee6JPTABz45gdI7g',
'Content-Type': 'application/json;charset=utf-8',
'Content-Length': '34',
'Host': 'api.xiaoyuzhoufm.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.2',
'x-jike-device-properties': '{"uuid":"b7686eb8-a596-4e95-b577-ba9ef07a5212","android_id":"6066ef25337fa198","oaid":"","vaid":"","aaid":""}',
'sentry-trace': '00000000000000000000000000000000-0000000000000000-0',
}


def sendCode(phone):
    url = 'https://api.xiaoyuzhoufm.com/v1/auth/sendCode'
    data = {
        "areaCode": "+86",
        "mobilePhoneNumber": phone
    }
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    text = json.loads(resp.text)
    if text == {}:
        print("send success")
    else:
        print("send fail:", text)


def login(phone, code):
    data = {
        "verifyCode": code,
        "areaCode": "+86",
        "mobilePhoneNumber": phone
    }
    url = "https://api.xiaoyuzhoufm.com/v1/auth/loginOrSignUpWithSMS"
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    return resp
    # text = json.loads(resp.text)
    # print(text)
    # {"data":{"isSignUp":false,"showNewbieGuide":true,"newbieGuideFeatureGroup":"SKIP","subscriptionGuideFeatureGroup":"DISABLED","user":{"type":"USER","uid":"648d8ad1edce67104af360b4","avatar":{"picture":{"picUrl":"https://image.xyzcdn.net/Fo4xvk1XtpoktwZbWRpEZb_gzDUO","largePicUrl":"https://image.xyzcdn.net/Fo4xvk1XtpoktwZbWRpEZb_gzDUO@large","middlePicUrl":"https://image.xyzcdn.net/Fo4xvk1XtpoktwZbWRpEZb_gzDUO@middle","smallPicUrl":"https://image.xyzcdn.net/Fo4xvk1XtpoktwZbWRpEZb_gzDUO@small","thumbnailUrl":"https://image.xyzcdn.net/Fo4xvk1XtpoktwZbWRpEZb_gzDUO@thumbnail","width":663,"height":663,"format":"png"}},"nickname":"HD221364x","isNicknameSet":false,"gender":"THIRD","isCancelled":false,"readTrackInfo":{},"phoneNumber":{"mobilePhoneNumber":"133****1260","areaCode":"+86"},"phoneNumberNeeded":false,"ipLoc":"广东","isInvited":true,"userCanDebug":false}}}


def getToken(resp):
    mapToken = resp.headers
    accessToken = mapToken['x-jike-access-token']
    refreshToken = mapToken['x-jike-refresh-token']
    return accessToken, refreshToken


# if __name__ == '__main__':
#     phone = "13360381260"
#     #sendCode(phone)\
#     login(phone, '4045')
