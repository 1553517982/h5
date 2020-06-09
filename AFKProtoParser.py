# -*- coding: cp936 -*-
#AES  
#��Կ 32e49bb599d12856714b5d2f910f4ae3
#ƫ�� 0123456789abcdef
#Mode CBC
#Block 128

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# ���text����16λ�ı������ÿո���Ϊ16λ
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# ���ܺ���
def encrypt(text):
    key = '32e49bb599d12856714b5d2f910f4ae3'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'0123456789abcdef'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # ��ΪAES���ܺ���ַ�����һ����ascii�ַ����ģ����������ܴ������⣬��������תΪ16�����ַ���
    return b2a_hex(cipher_text)


# ���ܺ�ȥ������Ŀո���strip() ȥ��
def decrypt(text):
    key = '32e49bb599d12856714b5d2f910f4ae3'.encode('utf-8')
    iv = b'0123456789abcdef'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    files = os.listdir("./")
    for fileName in files:
        if fileName.endswith('.proto'):
            with open(fileName,'r') as f:
                d = decrypt(f.read())  # ����
                print d        
    
    
