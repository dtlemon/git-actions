from flask import Flask, request
from datetime import datetime
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    page = """"""
    date_raw = datetime.now()
    date_pretty = date_raw.strftime("%m-%d-%Y")
    page += f"{date_pretty}"
    page += """
    <form action=/>
        <h1>Links:</h1>
        <br>
        <table>
            <tr>
                <td><a href="/calc">Calculator</a></td>
                <td><a href="/weather">Weather</a></td>
            </tr>  
        </table>
    </form>

    
    """
    return page

@app.route('/calc')
def calc():
    page = """
    <table>
        <tr>
            <td><a href="/">Back to Home</a></td>
            <td><a href="/weather">Weather</a></td>
        </tr>  
    </table>
    <br>
    <form action=/calc method=get>
        <input name=a />
        <select name="op" id="operator">
          <option value="+">+</option>
          <option value="-">-</option>
          <option value="*">*</option>
          <option value="/">/</option>
        </select>
        <input name=b />
        <input type=submit />
    </form>
    """

    try:
        a = int(request.args["a"])
        op = request.args["op"]
        b = int(request.args["b"])

        if (op == "+"):
            page += f"<p>Answer: {a+b}</p>"
        elif (op == "-"):
            page += f"<p>Answer: {a-b}</p>"
        elif (op == "*"):
            page += f"<p>Answer: {a*b}</p>"
        elif (op == "/"):
            page += f"<p>Answer: {a/b}</p>"
        else:
            pass

    except:
        pass
    return page
        
@app.route('/weather')
def weather():
    latitude = 40.107166238 
    longitude = -85.659664028
    page = """
        <table>
            <tr>
                <td><a href="/">Back to Home</a></td>
                <td><a href="/calc">Calculator</a></td>
            </tr>  
        </table>
        <br><br>
        <h1>The Weather at Anderson University today is:</h1>
        <br><br>
    """
    res = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    points = json.loads(res.text)
    forecast_url = points["properties"]["forecast"]

    res = requests.get(forecast_url)
    forecast = json.loads(res.text)
    current = forecast["properties"]["periods"][0]

    page += f"<h3>{current['detailedForecast']}</h3>"

    return page
