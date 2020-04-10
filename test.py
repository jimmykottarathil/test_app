from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('test.html', data=name)
    else:
        return render_template('test.html')

if __name__ == "__main__":
    app.run()
