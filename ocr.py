from aip import AipOcr

def baiduOCR(picfile):
    # picfile:图片文件名

    """ 你的 APPID AK SK """
    APP_ID = '25478049'
    API_KEY = '5DP0MmlLRpzdN7wOMWetALgW'
    SECRET_KEY = 'BkR5Ii8c5AxOOqndtjpssqGVGwBzsDVG'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(picfile, 'rb')
    img = i.read()
    message = client.general(img)
    i.close()

    # 输出文本内容
    for text in message.get('words_result'):  # 识别的内容
        a = text.get('words')
        with open('1.txt', "a+") as wfile:
            wfile.write(a)
            wfile.write('\n')
        return a


if __name__ == '__main__':
    baiduOCR('screen.png')

