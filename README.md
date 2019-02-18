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

# 添加解释器
```bash
sed -i "1i #!`which python3`" /usr/lib/zabbix/alertscripts/dingding.py
```

# 测试
命令行执行
```bash
./dingding.py --webhook=https://oapi.dingtalk.com/robot/send?access_token=e4bb4d6df22aae87d274c8786ac818363268b013d7052bf5993862acc415e671
```
如果钉钉上收到`test send msg`消息则正确

# zabbix设置
## 添加报警媒介
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding1.png)
## 添加动作--触发器
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding2.png)
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding3.png)
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding4.png)
消息内容
```bash
## {HOSTNAME1} 故障！

**告警等级：{TRIGGER.SEVERITY}**

告警信息: {TRIGGER.NAME} 

IP地址: {HOST.CONN} 

告警时间: {EVENT.DATE} {EVENT.TIME} 

持续时间: {EVENT.AGE}

告警项目: {TRIGGER.KEY1} 

事件ID: {EVENT.ID} 

问题详情: {ITEM.NAME}

检测值: 
> # {ITEM.VALUE}
```
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding5.png)
消息内容
```bash
## {HOSTNAME1} 恢复！

**告警等级：{TRIGGER.SEVERITY}**

告警信息: {TRIGGER.NAME} 

IP地址: {HOST.CONN} 

恢复时间: {EVENT.DATE} {EVENT.RECOVERY.TIME} 

持续时间: {EVENT.AGE}

告警项目: {TRIGGER.KEY1} 

事件ID: {EVENT.ID} 

问题详情: {ITEM.NAME}

检测值: 
> # {ITEM.VALUE}
```
## 添加用户报警媒介
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding6.png)

# 结果展示
![](https://raw.githubusercontent.com/hcxcloud/zaxdd/master/img/dingding7.png)
