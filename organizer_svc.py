# coding utf-8
import requests
from flask import Flask


app = Flask(__name__)


if app.config['ENV'] == "development":
    CHECK_TEMP_SVC = 'http://192.168.1.100:8082/check_temp'
    SENSOR = 'http://192.168.1.100:8083/'
else:
    CHECK_TEMP_SVC = 'http://tempcheck:8080/check_temp'
    SENSOR = 'http://sensor:8080/'


@app.route('/measure_temperature', methods=['POST'])
def measure_temperature():

    # sense temperature
    try:
        response = requests.get(
            SENSOR,
            timeout=1.0
        )
        response_post = requests.post(
            'http://m2x:8080/machinist', None,
            response.json()
        )
        return response_post.json()
    except Exception as e:
        print('=== エラー内容 ===')
        print('type:' + str(type(e)))


@app.route('/check_temperature', methods=['GET'])
def check_temperature():

    # check temperature
    message = requests.get(
        CHECK_TEMP_SVC
    )

    # send message thru line
    response_post = requests.post(
        'http://line:8080/send_msg', None,
        message.json()
    )

    return response_post.json()


@app.route('/', methods=['POST'])
def organize():
    # GETパラメータはparams引数に辞書で指定する

    response = requests.get(
        'http://sensor:8080/'
    )

    # レスポンスオブジェクトのjsonメソッドを使うと、
    # JSONデータをPythonの辞書オブジェクトを変換して取得できる。
    # response_json = response.json()
    # temperature = response_json['value']['temperature']
    # humidity = response_json['value']['humidity']
    # pprint.pprint(response.json())
    # print(temperature, humidity)

    response_post = requests.post(
        'http://m2x:8080/m2x', None,
        response.json()
    )
    # pprint.pprint(response_post.json())

    return response_post.json()


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8080)
