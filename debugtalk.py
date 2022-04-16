import socket
import struct
import time
import random

global userName, userPassword, DeviceName
userName = ''
userPassword = ''


def getfile():
    return open(file="要打开的文件的路径", mode="rb")


def sleep(response, n_secs):
    if response.status_code == 200:
        time.sleep(n_secs)
    else:
        time.sleep(1)


def get_userName():
    global userName
    userName = ''.join(
        random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/", 8))
    return userName


def get_userPassword():
    global userPassword
    userPassword = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890", 6))
    return userPassword


def get_DeviceName():
    global DeviceName
    DeviceName = ''.join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890", 6))
    return DeviceName



#获取组播地址
RANDOM_IP_multicast_POOL = ['232.10.100.222/24', '232.20.100.222/24', '232.168.30.222/24', '232.40.100.222/24']


def get_random_multicast_ip():
    str_ip = RANDOM_IP_multicast_POOL[random.randint(0, len(RANDOM_IP_multicast_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | (1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))


#获取IP地址
RANDOM_IP_POOL = ['192.10.100.222/24']


def get_random_ip():
    str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | (1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))


if __name__ == '__main__':
    mul_ip = get_random_multicast_ip()
    ip = get_random_ip()
    print(socket.inet_aton('192.10.100.222'))
    print(ip)
    print(get_DeviceName())


