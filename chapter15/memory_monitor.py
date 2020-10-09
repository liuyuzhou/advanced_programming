import psutil

from email.mime.text import MIMEText
import smtplib
from email.header import Header


def mem():
    """
    监控内存信息
    :return:
    """
    mem_total = int(psutil.virtual_memory()[0]/1024/1024)
    mem_used = int(psutil.virtual_memory()[3] / 1024 / 1024)
    mem_per = (mem_used / mem_total) * 100
    mem_info = {
		'mem_total' : mem_total,
		'mem_used' : mem_used,
		'mem_per' : mem_per
	}
    return mem_info


def send_email(info):
    sender = 'test@163.com'
    pwd = 'test'
    receivers = ['abc@163.com']

    subject = '监控报警'
    msg = MIMEText(info, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receivers[0]

    try:
        # 使用非本地服务器，需要建立ssl连接
        smtp_obj = smtplib.SMTP_SSL("smtp.163.com", 465)
        # smtp_obj.login(sender, pwd)
        # smtp_obj.sendmail(sender, receivers, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(f"Error: 无法发送邮件.Case:{e}")


def cpu():
    """
    监控cpu信息
    :return:
    """
    # 每秒cpu使用率，（1，True） 每一核cpu的每秒使用率
    cpu_per = int(psutil.cpu_percent(1))
    return cpu_per


def monitor_info():
    cpu_info = cpu()
    mem_info = mem()
    info = f'''
				监控信息
		=========================
		cpu使用率： : {cpu_info},
		=========================
		内存总大小（MB） : {mem_info['mem_total']},
		内存使用大小（MB） : {mem_info['mem_used']},
		内存使用率 : {mem_info['mem_per']: 0.2f}%,
	'''
    print(info)
    is_danger = False
    if mem_info['mem_per'] > 50:
        send_email(info)
        is_danger = True
    return is_danger


if __name__ == "__main__":
    monitor_info()
