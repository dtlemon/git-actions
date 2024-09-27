from flask import Flask, request
from datetime import datetime

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
    </form>

    
    """
    return page

@app.route('/calc')
def calc():
    # a = int(request.args["a"])
    # b = int(request.args["b"])
# 
    # return f"{a + b}"
    page = """
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
