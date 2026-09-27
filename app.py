from flask import Flask

app = Flask(__name__)

MESSAGE = "Hello from Harness CI!"


@app.route("/")
def hello():
    return MESSAGE


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
