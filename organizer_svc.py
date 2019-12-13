# coding utf-8
import requests
from flask import Flask


app = Flask(__name__)


@app.route('/measure_temperature', methods=['POST'])
def post():

    # sense temperature
    response = requests.get(
        'http://sensor:8080/'
    )

    # send temperature to m2x
    response_post = requests.post(
        'http://m2x:8080/m2x', None,
        response.json()
    )

    return response_post.json()


@app.route('/check_temperature', methods=['POST'])
def post():

    # check temperature
    message = requests.post(
        'http://tempcheck:8080/check_temp'
    )

    # send message thru line
    response_post = requests.post(
        'http://line:8080/send_msg/', None,
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
