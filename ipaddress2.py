import pysnooper
import ipaddress

@pysnooper.snoop()
def get_ip_network(ipaddr):
    my_ip = ipaddress.ip_interface(ipaddr.decode())
    my_ip_net = ipaddress.ip_network(my_ip,strict=False)
    return my_ip_net

aa = get_ip_network(200.200.1.2)