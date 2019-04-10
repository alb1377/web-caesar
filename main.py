from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post">
        <label>Rotate by:</label>
        <input type="text" name="rot">
        <br>
        <br>
        <textarea name="text">{0}</textarea>
        <br>
        
        <input type="submit">
      </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format()

@app.route("/", methods=['POST'])
def encrypt():
    parameter1 = int(request.form['rot'])
    parameter2 = request.form['text']
    ciphered = "<h1>" + rotate_string + "</h1>"
    return form.format(ciphered)
app.run()