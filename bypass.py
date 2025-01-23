from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/addlink', methods=['GET'])
def add_link():
    url = request.args.get('url')
    if url:
        start_time = time.time()
        duration = time.time() - start_time
        return f'{{"status":"success","result":"Api Bypass Is In Progress","duration":"{duration:.6f}"}}'
    else:
        return f'{{"status":"error","result":"Missing URL parameter"}}', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
