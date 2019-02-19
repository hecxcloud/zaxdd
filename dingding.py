import sys
import argparse
import requests


def para():
    parser = argparse.ArgumentParser(prog='dingding', description='help manual')
    parser.add_argument('--webhook', type=str, default=None, help='钉钉机器人url')
    parser.add_argument('--title', type=str, default='zabbix message', help='标题')
    parser.add_argument('--msg', type=str, default='test send msg', help='POST消息( default：test send msg)')
    parser.add_argument('--at', type=str, default='', help='指定接收人的手机号，如果多个请用英文逗号分隔')
    args = parser.parse_args()
    a = args.webhook
    b = args.title
    c = args.msg
    d = args.at.split(',')

    if not a:
        print('url为空')
        sys.exit()

    return a, b, c, d


def send_msg(url, msg, title, at):
    data = {
        'msgtype': 'markdown',
        'markdown': {
            'title': title,
            'text': msg
        },
        'at': {
            'atMobiles': at,
            'isAtALL': 'false'
        }
    }

    requests.post(url, json=data)


if __name__ == '__main__':
    url, title, msg, at = para()
    send_msg(url, msg, title, at)
