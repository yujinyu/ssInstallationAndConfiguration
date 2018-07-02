#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from config_ss_redir import modify_conf
from conf import ss_or_ssr

if __name__ == "__main__":
    current_dir = os.getcwd()
    help(os.execl)
    #os.system("sh %s %s" %(os.path.join(current_dir, "install_pkgs.sh") , current_dir))
    #modify_conf(ss_or_ssr == "ssr")
    print("Succeed in  Installing  and configuring  ss-redir! \nPlease Run Comand \"ss-tproxy start\" to use ss-tproxy.")
