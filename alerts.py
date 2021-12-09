import os
import pandas
import requests
import random
import smtplib

from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 6812.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.153 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASAJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Linux; Android 4.4.2; SM-T210R Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.18.US Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.22 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; SM-T350 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/7.0; 1ButtonTaskbar)",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG-SM-G920A Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0 Chrome/38.0.2125.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36"
]


def send_email_alert(content):
    """Send an email alert."""
    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], os.environ['SMTP_PORT']) as smtp:
        smtp.starttls()
        smtp.login(os.environ['FROM_EMAIL'], os.environ['FROM_EMAIL_PW'])
        smtp.sendmail(
            to_addrs=os.environ['TO_EMAIL'],
            from_addr=os.environ['FROM_EMAIL'],
            msg=f"Subject: Lazada price drop detected!\n\n{content}"
        )


def main():
    try:
        data = pandas.read_csv(os.environ['DATA_FILE'])
    except (FileNotFoundError, KeyError):
        print("Error: Data not found.\n"
              "Please read the instructions on how to run this script.\n"
              "Link: https://github.com/ngeks/lazada-price-drop-alerts")
    else:
        no_price_drop_detected = True
        number_of_alerts = 0

        for (idx, data) in data.iterrows():
            print(f"Task: Looking for {data['name']} price.")

            try:
                resp = requests.get(data['url'], headers={'User-Agent': random.choice(USER_AGENTS)})
                bs = BeautifulSoup(resp.text, "html.parser")
                html = bs.find("span", class_="pdp-price")
                price_text = html.get_text()[1:]
            except requests.exceptions.ConnectTimeout:
                print("Error: Server took too long to respond.\n")
            except AttributeError:
                print(f"Result: {data['name']} price not found. Skipped.\n")
            else:
                current_price = float(price_text.replace(",", ""))

                if current_price < data['price']:
                    no_price_drop_detected = False
                    percentage = round(((data['price'] - current_price) / data['price']) * 100, 2)
                    print(f"Result: {percentage}% price drop detected.\n")
                    print("Task: Attempting to send an email.")
                    try:
                        send_email_alert(f"Product Name: {data['name']}\n"
                                         f"Product URL: {data['url']}\n"
                                         f"Result: {percentage}% price drop detected.")
                    except (smtplib.SMTPServerDisconnected, KeyError):
                        print("Error: SMTP Client is not configured properly.\n")
                    except TimeoutError:
                        print("Error: A connection attempt failed.\n")
                    except smtplib.SMTPResponseException as e:
                        print(f"Error: Sending email failed. (Error Code: {e.smtp_code})\n")
                    else:
                        print("Result: Success. An email has been sent.\n")
                        number_of_alerts += 1
                else:
                    print(f"Result: No price drop detected.\n")

        if data.empty:
            print("Error: Your data is empty. There is nothing to do here.")
        elif no_price_drop_detected:
            print("Notice: No price drop detected for any of your products.\n")
        print(f"===> A total of {number_of_alerts} alerts has been sent. <===")


if __name__ == "__main__":
    main()
    