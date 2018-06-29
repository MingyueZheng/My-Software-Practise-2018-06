from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11464720'
API_KEY = 'tE6GZK1kzn1jsIxQx6QkGgTV'
SECRET_KEY = 'w5WX0AihBf1sRcsn8bMsjgkzuMhUepqF '

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = aipSpeech.asr(get_file_content(r'16k-23850.amr'), 'amr', 16000,{'lan': 'zh',})
print(result['result'][0])
print(result)

result = aipSpeech.synthesis('郑明月，杨欣宇，杜培，乔佳楠，王若晗，蒋浩俊','zh','1',{'vol':5})
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)