import json
from flask import Flask, request
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

def bypass_linkvertise(url):
    try:
        chrome_options = Options()
chrome_options.binary_location = "C:\Users\Administrator\Downloads\ChromeSetup.exe"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.get(url)

        time.sleep(5)

        final_url = driver.current_url
        driver.quit()

        if "linkvertise" not in final_url:
            return {"status": "success", "result": final_url}
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

        return f'<pre style="font-family: monospace;">{json.dumps(result, separators=(",", ":"))}</pre>'
    else:
        duration = 0.0
        error_result = {
            "status": "error",
            "result": "Missing URL parameter",
            "duration": f"{duration:.16f}"
        }
        return f'<pre style="font-family: monospace;">{json.dumps(error_result, separators=(",", ":"))}</pre>', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
