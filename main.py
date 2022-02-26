import pymysql
import schedule
import time
from app import app
from db_config import mysql
from flask import jsonify
from triggers import proxy_trigger


@app.route('/', methods=['GET'])
def add_user():
    proxy_trigger.add_new_proxies()
    print('triggered')
    return "New Proxy has been added !"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9531)
