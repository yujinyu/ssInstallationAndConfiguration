#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from conf import *


def format_str(str):
    return "\'" + str + "\'\n"


def modify_conf(is_ssr):
    conf_file = "/etc/tproxy/ss-tproxy.conf"
    fp = open(conf_file, 'r', encoding='utf-8')
    txt = fp.readlines()
    fp.close()
    modified_txt = []
    for line in txt:
        if "server_addr=" in line:
            if is_ssr:
                line = line[0:len('server_addr=')] + format_str(ssr_server_addr)
            else:
                line = line[0:len('server_addr=')] + format_str(ss_server_addr)
        elif "server_port=" in line:
            if is_ssr:
                line = line[0:len('server_port=')] + format_str(ssr_server_port)
            else:
                line = line[0:len('server_port=')] + format_str(ss_server_port)
        elif "server_method=" in line:
            if is_ssr:
                line = line[0:len('server_method=')] + format_str(ssr_server_method)
            else:
                line = line[0:len('server_method=')] + format_str(ss_server_method)
        elif "server_passwd=" in line:
            if is_ssr:
                line = line[0:len('server_passwd=')] + format_str(ssr_server_passwd)
            else:
                line = line[0:len('server_passwd=')] + format_str(ss_server_passwd)
        elif "server_use_ssr=" in line:
            if is_ssr:
                line = line[0:len('server_use_ssr=')] + format_str("true")
            else:
                line = line[0:len('server_use_ssr=')] + format_str("false")
        elif "server_protocol=" in line:
            if is_ssr:
                line = line[0:len('server_protocol=')] + format_str(ssr_server_protocol)
        elif "server_protocol_param=" in line:
            if is_ssr:
                line = line[0:len('server_protocol_param=')] + format_str(ssr_server_protocol_param)
        elif "server_obfs=" in line:
            if is_ssr:
                line = line[0:len('server_obfs=')] + format_str(ssr_server_obfs)
        elif "server_obfs_param=" in line:
            if is_ssr:
                line = line[0:len('server_obfs_param=')] + format_str(ssr_server_obfs_param)
        elif "chinadns_upstream=" in line:
            line = line.replace("114.114.114.114", dns1_in_your_network)
        elif "iptables_intranet=" in line:
            line = line[0:len("iptables_intranet=")] + subnet_mask
        elif "dns_original=" in line:
            line = line.replace("119.29.29.29", dns1_in_your_network)
            line = line.replace("180.76.76.76", dns2_in_your_network)
        modified_txt.append(line)
    fp = open(conf_file,'w',encoding='utf-8')
    for line in modified_txt:
        fp.write(line)
    fp.close()
