#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,hashlib,time,base64,codecs,json

MOD = 256

def KSA(key):
    key_length = len(key)
    # create the array "S"
    S = range(MOD)  # [0,1,2, ... , 255]
    j = 0
    for i in range(MOD):
        j = (j + S[i] + ord(key[i % key_length])) % MOD
        S[i], S[j] = S[j], S[i]  # swap values

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % MOD]
        yield K


def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)


def encrypt(key, plaintext):
    keystream = get_keystream(key)

    res = []
    for c in plaintext:
        val = ("%02X" % (ord(c) ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)


def decrypt(key, ciphertext):
    ''' :key -> encryption key used for encrypting, as hex string
        :ciphertext -> hex encoded ciphered text using RC4
    '''
    ciphertext = base64.b64decode(ciphertext)
    #print 'ciphertext to func:', ciphertext  # optional, to see
    res = encrypt(key, ciphertext)
    return res.decode('hex')


def main():
    key = "5fdd79763095baae440e87f7e1789d18"
    with open('com.BNchuanqi.game') as file_obj:
        content = file_obj.read()
        jobj=json.loads(content)
        userdata = jobj["content"]
        decrypted = decrypt(key, userdata)
        with codecs.open('out.txt',"w") as f:
                f.write(decrypted)
                    

if __name__ == '__main__':
    main()
