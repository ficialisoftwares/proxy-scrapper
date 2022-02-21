import time
from proxy_source.cagriari import cagriari_proxy
from proxy_source.proxy_list import proxy_list
from utils.presistance_tools.database.db_connection import DatabaseConnection
from datetime import datetime
from threading import Thread
import keyboard


def get_fresh_proxy(connection):

    calgriari_proxies = cagriari_proxy.get_proxies()
    proxy_list_proxies = proxy_list.get_proxies()
    new_proxies = calgriari_proxies + proxy_list_proxies
    for proxy_address in new_proxies:
        try:
            proxy_query = "INSERT INTO proxy (address,expiry_status) VALUES ('" + proxy_address + "',False);"
            connection.query(proxy_query)

        except Exception as e:
            print(e)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Latest Proxy added ! ==> ", str(current_time))


def reload_fresh_proxy(connection):
    proxy_query = "SELECT address from proxy where expiry_status IS false LIMIT 30;"
    result = connection.select_query(proxy_query)
    return result


def update_expired_status(address,connection):
    proxy_query = "UPDATE proxy SET expiry_status = True, updated_on = now() where address = '{}';".format(str(address))
    connection.query(proxy_query)


def update_multiple_expired_status(proxy_list,connection):

    for address in proxy_list:
        proxy_query = "UPDATE proxy SET expiry_status = True, updated_on = now() where address = '{}';".format(str(address))
        connection.query(proxy_query)

    print("Expired proxies updated !")

def start_proxy_thread(main_connection):
    t3 = Thread(target=get_fresh_proxy,args=(main_connection,))
    t3.start()
    t3.join()

