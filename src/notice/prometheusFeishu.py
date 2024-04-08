# -*- coding: utf-8 -*-
__author__ = 'shensg168@gmail.com'

from notice import send


def feishu(title="PrometheusAlert",
           webhook=None,
           old_alert=None,
           new_alert=None,
           old_prometheus=None,
           new_prometheus=None,
           data=dict):
    print(str(old_prometheus[0]), str(new_prometheus[0]))

    if "测试告警" in data.get("text"):
        image = "img_v3_025s_6be37f73-896f-4b0f-950f-533decfeff9g"
        content = data.get("text")
        r_post = send.fs_notice(image, title, content, webhook)
        print(r_post)

    elif "Prometheus恢复信息" in data.get("text"):
        image = "img_v3_025s_bdc4954d-e00b-4d4f-9b01-0d1eaf3d0ddg"
        content = data.get("text")
        if old_alert and new_alert:
            content = str(content).replace(str(old_prometheus[0]), str(new_prometheus[0]))
        if old_prometheus and new_prometheus:
            content = str(content).replace(str(old_alert[0]), str(new_alert[0]))
        r_post = send.fs_notice(image, title, content, webhook)
        print(r_post)

    else:
        image = "img_v3_025s_6be37f73-896f-4b0f-950f-533decfeff9g"
        content = data.get("text")
        if old_alert and new_alert:
            content = str(content).replace(str(old_prometheus[0]), str(new_prometheus[0]))
        if old_prometheus and new_prometheus:
            content = str(content).replace(str(old_alert[0]), str(new_alert[0]))
        r_post = send.fs_notice(image, title, content, webhook)
        print(r_post)

    # return res
