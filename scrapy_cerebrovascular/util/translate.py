import random
import time  # 时间戳
import json  # 返回json 处理
import requests  # 请求 url
import hashlib  # md5 加密
import re


# def translate(word):
#     # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#     # 有道翻译的　API
#     word = word.lower()
#     word = re.sub(r'\n', '|', word)
#     t = str(int(time.time() * 1000))  # 当前时间戳
#     s = "sr_3(QOHT)L2dx#uuGR@r"  # 一段用来加密的字符串
#     sign_ = "fanyideskweb" + word + t + s
#     m = hashlib.md5()  # 根据数据串的内容进行 md5 加密
#     m.update((sign_).encode('utf-8'))
#     # print(m.hexdigest())
#     word_key = {  # key 这个字典为 POST 给有道词典服务器的内容
#         'i': word,
#         'from': 'AUTO',
#         'to': 'AUTO',
#         'smartresult': 'dict',
#         'client': 'fanyideskweb',
#         'salt': t,
#         'sign': m.hexdigest(),
#         'doctype': 'json',
#         'version': '2.1',
#         'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_CLICKBUTTION',
#         'typoResult': 'false'
#     }
#     response = requests.post(url, data=word_key)  # 发送请求
#     # print(response)
#     # 判断服务器是否相应成功
#     if (response.status_code == 200):
#         # print(response.text)
#         if word:
#             # print(response.text)
#             try:
#                 result_list = json.loads(response.text).get("translateResult")
#                 if [i['tgt'] for i in result_list[0]]:
#                     return ''.join([i['tgt'] for i in result_list[0]])
#             except Exception as err:
#                 print(f'err:{err}, word:{word}')
#             return ''
#         return ''
#         # if response.text:
#         #     result_list = json.loads(response.text)
#         #     if result_list:
#         #         result_list = result_list.get("translateResult")
#         #     if result_list and not [i['tgt'] for i in result_list[0]]:
#         #         return ''.join([i['tgt'] for i in result_list[0]])
#         # return ''
#     else:
#         print("有道 API 调用失败")
#         return None


def translate(word):
    word = re.sub(r'\n', '|', word)
    word = word.lower()
    # set baidu develop parameter
    apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    appid = '20201218000650218'
    secretKey = '6QDHOEEGLRqSvc7JeuRk'
    time.sleep(1)
    return translateBaidu(apiurl, appid, secretKey, word, 'en', 'zh')


# 翻译内容 源语言 翻译后的语言
def translateBaidu(apiurl, appid, secretKey, content, fromLang='en', toLang='zh'):
    salt = str(random.randint(32768, 65536))
    sign = appid + content + salt + secretKey  # appid+q+salt+密钥 的MD5值
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()  # 对sign做md5，得到32位小写的sign

    try:
        # 根据技术手册中的接入方式进行设定
        paramas = {
            'appid': appid,
            'q': content,
            'from': fromLang,
            'to': toLang,
            'salt': salt,
            'sign': sign
        }
        response = requests.get(apiurl, paramas)

        jsonResponse = json.loads(response.text)  # 获得返回的结果，结果为json格式
        # print(content)
        # print(jsonResponse)
        dst = jsonResponse.get('trans_result')[0]["dst"]
        # dst = str(jsonResponse["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        # print(dst)
        return dst
    except Exception as e:
        print(e, '1')
        print(content)


def get_word_result(word):
    print(word)
    # word_result = json.loads(word)

    # 通过　json.loads 把返回的结果加载成 json 格式
    # print(word_result)
    # print("输入的词为：" + word_result["translateResult"][0][0]['src'])
    # print("翻译结果为：" + word_result["translateResult"][0][0]['tgt'])


def main():
    print("欢迎使用，本程序调用有道词典 API 进行翻译\n自动检测输入语言-->中文\n中文-->英文")
    while (True):
        word = str(input("请输入你想翻译的词或者句子(输入 q 退出)："))
        if (word == 'q'):
            print("感谢使用")
            break
        word_ = translate(word)
        get_word_result(word_)


if __name__ == '__main__':
    # main()
    translate('unknown status')
