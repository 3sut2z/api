from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/api-bypass/addlink', methods=['GET'])
def add_link():
    url = request.args.get('url')
    if url:
        start_time = time.time()
        duration = time.time() - start_time
        return f'<pre style="font-family: monospace;">{{"status":"success","result":"Api Bypass Is In Progress","duration":"{duration:.16f}"}}</pre>'
    else:
        return f'<pre style="font-family: monospace;">{{"status":"error","result":"Missing URL parameter"}}</pre>', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
