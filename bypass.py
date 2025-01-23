from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/addlink', methods=['GET'])
def add_link():
    url = request.args.get('url')
    if url:
        start_time = time.time()

        duration = time.time() - start_time
        return jsonify({"status": "success", "result": "Api Bypass Is In Progress", "duration": f"{duration:.6f}"})
    else:
        return jsonify({"status": "error", "message": "Missing URL parameter"}), 400

if __name__ == '__main__':
    app.run(debug=True)
