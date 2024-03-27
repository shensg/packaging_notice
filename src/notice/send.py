# -*- coding: utf-8 -*-

import requests
import json

__author__ = "shensg168@gmail.com"


def fs_notice(image, title, content, webhook):
    card = json.dumps({
        "config": {
            "wide_screen_mode": True
        },
        "elements": [{
            "alt": {
                "content": "",
                "tag": "plain_text"
            },
            "img_key": image,
            "tag": "img"
        },
            {
                "tag": "div",
                "text": {
                    "content": content,
                    "tag": "lark_md"
                }
            }
        ],
        "header": {
            "title": {
                "content": title,
                "tag": "plain_text"
            },
            "template": "red"
        }
    })
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/" + webhook
    body = json.dumps({"msg_type": "interactive", "card": card})
    headers = {"Content-Type": "application/json"}
    r_post = requests.post(url=url, data=body, headers=headers)
    print(r_post)
    return r_post
