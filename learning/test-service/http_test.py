from flask import Flask, jsonify, request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host", default="127.0.0.1")
parser.add_argument("--port", default="28000", type=int)
parser.add_argument("--debug", default="0", type=int)


class Service:

    def __init__(self):
        self.app = Flask(__name__)
        self.args = parser.parse_args()

        self.app.add_url_rule('/echo', 'echo', self.print_ext, methods=['POST'])

    @staticmethod
    def print_ext():
        print request.json
        return jsonify({'status': 'success', 'data': request.json})

    def run(self):
        try:
            self.app.run(host=self.args.host, port=self.args.port, debug=self.args.debug != 0)
        except KeyboardInterrupt:
            exit(1)


serviceObj = Service()
serviceObj.run()