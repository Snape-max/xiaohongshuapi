from utils import HongshuParser
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有域名访问
api = Api(app)


class Parser(Resource):
    def get(self, url, type):
        if type == "short":
            url = "http://xhslink.com/" + url
        elif type == "long":
            url = "https://www.xiaohongshu.com/explore/" + url
        else:
            return {}
        return HongshuParser(url)

api.add_resource(Parser, '/api/v1/image/<string:type>/<string:url>')

@app.route('/')
def index():
    return """<center><h1>Xiao Hongshu api</h1></center>
    <br>
    <br>
    <center><h2>图片解析</h2></center>
    <center><p>短连接: 请求：<code>/api/v1/image/short/<链接码></code></p></center>
    <center><p>长连接: 请求：<code>/api/v1/image/long/<链接码></code></p></center>
    """


if __name__ == '__main__':
    app.run()