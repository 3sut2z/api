from flask import Flask, request, jsonify
import time
import requests

app = Flask(__name__)

def bypass_linkvertise(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 302 or "location" in response.headers:
            original_url = response.headers["location"]
            return {"status": "success", "result": original_url}
        else:
            return {"status": "error", "result": "Unable to bypass Linkvertise URL"}
    except Exception as e:
        return {"status": "error", "result": str(e)}

@app.route('/api-bypass/addlink', methods=['GET'])
def add_link():
    url = request.args.get('url')
    if url:
        start_time = time.time()

        result = bypass_linkvertise(url)

        duration = time.time() - start_time
        result["duration"] = f"{duration:.16f}"

        return f'<pre style="font-family: monospace;">{result}</pre>'
    else:
        duration = 0.0
        return f'<pre style="font-family: monospace;">{{"status":"error","result":"Missing URL parameter","duration":"{duration:.16f}"}}</pre>', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
