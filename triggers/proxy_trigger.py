from db_config import mysql
from scrappers.proxy_source import cagriari_proxy, proxy_list

def add_new_proxies():
    proxy_one = cagriari_proxy.get_proxies()
    proxy_two = proxy_list.get_proxies()
    proxies = proxy_one + proxy_two
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        for proxy_address in proxies:
            try:
                sql = "INSERT INTO proxy_address(ip) VALUES(%s)"
                data = proxy_address
                cursor.execute(sql, data)
                conn.commit()

            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
