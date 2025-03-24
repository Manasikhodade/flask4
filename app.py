

import logging
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    app.logger.info(f"Received {request.method} request")

    result = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            if number % 2 == 0:
                result = f'{number} is Even'
            else:
                result = f'{number} is Odd'
        except ValueError:
            result = "Please enter a valid integer."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
