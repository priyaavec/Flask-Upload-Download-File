from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download_file():
    path = "sample.jpg"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5001, debug=True)