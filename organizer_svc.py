# coding utf-8
import requests
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['POST'])
def organize():
    # GETパラメータはparams引数に辞書で指定する

    response = requests.get(
        'http://192.168.1.100:8080/'
    )

    # レスポンスオブジェクトのjsonメソッドを使うと、
    # JSONデータをPythonの辞書オブジェクトを変換して取得できる。
    # response_json = response.json()
    # temperature = response_json['value']['temperature']
    # humidity = response_json['value']['humidity']
    # pprint.pprint(response.json())
    # print(temperature, humidity)

    response_post = requests.post(
        'http://192.168.1.100:8081/m2x', None,
        response.json()
    )
    # pprint.pprint(response_post.json())

    return response_post.json()


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8080)