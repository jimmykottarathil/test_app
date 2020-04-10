from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return render_template('test.html', data="JIMMY")
    else:
        return render_template('test.html')

if __name__ == "__main__":
    app.run()