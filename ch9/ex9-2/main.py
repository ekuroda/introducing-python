from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    v = {k: request.values.get(k) for k in ('things', 'height', 'color')}
    return render_template('./index.html', **v)


app.run(port=5000, debug=True)
