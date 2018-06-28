#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from config_ss_redir import modify_conf
from conf import ss_or_ssr

if __name__ == "__main__":
    # install necessary packages
    os.system("sed -i 's/\r/''/g' install_pkgs.sh")
    os.system("apt-get install -y  curl ipset iproute2 pdnsd haveged git \
                        gettext gcc autoconf libtool automake make perl wget  \
                        cmake asciidoc xmlto  libc-ares-dev libssl-dev libev-dev libpcre3 \
                        libpcre3-dev")
    os.system("apt-get autoremove -y")
    current_dir = os.getcwd()

    os.system("sh %s %s" %(os.path.join(current_dir, "install_pkgs.sh") , current_dir))
    modify_conf(ss_or_ssr)
    print("Succeed in  Installing  and configuring  ss-redir! \nPlease Run Comand \"ss-tproxy start\" to use ss-tproxy.")
