import sys
import mysql.connector

from time import gmtime, strftime
from proxy_source import cagriari_proxy, proxy_list

try:
    conn = mysql.connector.connect(
        user="maazqkxy_dev",
        password="#KyQM#T(Gc4E",
        host="localhost",
        port=3306,
        database="maazqkxy_proxy_host"
    )
except Exception as ex:
    print("An error occurred while connecting to " + ex)
    sys.exit(1)


def add_new_proxies():
    print('\nAdding new proxies triggered.')
    proxy_one = cagriari_proxy.get_proxies()
    proxy_two = proxy_list.get_proxies()
    proxies = proxy_one + proxy_two

    cursor = conn.cursor()
    try:
        ip_count = 0
        for proxy_address in proxies:
            try:
                cursor.execute(
                    "SELECT ip, COUNT(*) FROM proxy WHERE ip = %s GROUP BY ip",
                    (proxy_address,)
                )
                results = cursor.fetchall()
                row_count = cursor.rowcount

                if row_count == 0:
                    ip_count = ip_count + 1
                    sql = "INSERT INTO proxy(ip) VALUES(%s)"
                    data = [(proxy_address)]
                    cursor.execute(sql, data)
                    conn.commit()

            except Exception as e:
                print('Exception from base 1')
                print(e)

        print('\nCron Job added total {} new proxy address'.format(ip_count))

    except Exception as e:
        print('Exception from base 2')
        print(e)

    finally:
        cursor.close()
        conn.close()

    print('\nScheduler function finished  at {} '.format(
        strftime("%Y-%m-%d %H:%M:%S", gmtime())))


if __name__ == "__main__":
    print("\nCron Job began at {} EST time.".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    add_new_proxies()
