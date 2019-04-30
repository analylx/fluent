import pysnooper

@pysnooper.snoop(prefix='A:')
def str_to_hex(s):
    return ''.join([hex(ord(c)).replace('0x', '') for c in s])


@pysnooper.snoop(prefix='B:')
def m2u(mac_address):
    k = list(mac_address)
    k.insert(6, 'fffe')
    eui64 = ''.join(k)
    return eui64


if __name__ == '__main__':
    print(str_to_hex(m2u("00208f112233")))