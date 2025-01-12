import rmquote
from flask import Flask, send_file

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memcached://localhost:11211",
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/quote/pDw4y9YgKoC")
@limiter.limit("100 per day")
def quote():
    rmquote.genquote()
    return send_file("quote.png", mimetype='image/png')

if __name__ == "__main__": 
    app.run()