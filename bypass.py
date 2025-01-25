import json
from flask import Flask, request
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

def bypass_fluxus(start_url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        if "https://flux.li/android/external/start.php" in start_url and "HWID=" in start_url:
            
            driver.get("https://linkvertise.com/580726/fluxus1")
            time.sleep(2)
            
            driver.get("https://flux.li/android/external/check1.php?hash=")
            time.sleep(2)
            
            driver.get("https://linkvertise.com/580726/fluxus")
            time.sleep(2)
            
            driver.get("https://flux.li/android/external/main.php?hash=")
            time.sleep(2)
            
            final_url = driver.current_url
            driver.quit()
            return {"status": "success", "result": final_url}
        else:
            return {"status": "error", "result": "Invalid URL"}
    except Exception as e:
        return {"status": "error", "result": str(e)}

@app.route('/api-bypass/addlink', methods=['GET'])
def add_link():
    url = request.args.get('url')
    if url:
        start_time = time.time()

        result = bypass_fluxus(url)

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
