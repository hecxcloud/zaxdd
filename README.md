# zaxdd
![](https://img.shields.io/badge/-Python3-green.svg)
![](https://img.shields.io/badge/-Zabbix3.4%2B-red.svg)

zabbix3.4+钉钉报警

# 安装依赖
```bash
pip3 install requests
```

# 下载&授权
```bash
cd /tmp && git clone https://github.com/hcxcloud/zaxdd.git
mv /tmp/zaxdd/dingding.py /usr/lib/zabbix/alertscripts/
chown zabbix.zabbix /usr/lib/zabbix/alertscripts/dingding.py
chmod +x /usr/lib/zabbix/alertscripts/dingding.py
```

# zabbix设置
## 
