'''
rss_reddit_imgdl.py
Hussein Esmail
Created: 2021 11 11
Updated: 2022 01 01
'''

import os               # Used for checking file paths
import sys              # Used for exiting program and temporary print lines
import time

# ========= COLOR CODES =========
color_end               = '\033[0m'
color_darkgrey          = '\033[90m'
color_red               = '\033[91m'
color_green             = '\033[92m'
color_yellow            = '\033[93m'
color_blue              = '\033[94m'
color_pink              = '\033[95m'
color_cyan              = '\033[96m'
color_white             = '\033[97m'
color_grey              = '\033[98m'

# ========= COLORED STRINGS =========
str_prefix_q            = f"[{color_pink}Q{color_end}]"
str_prefix_y_n          = f"[{color_pink}y/n{color_end}]"
str_prefix_ques         = f"{str_prefix_q}\t "
str_prefix_err          = f"[{color_red}ERROR{color_end}]\t "
str_prefix_done         = f"[{color_green}DONE{color_end}]\t "
str_prefix_info         = f"[{color_cyan}INFO{color_end}]\t "

# ========= LOADING STRINGS =========
don0 = f"[{color_cyan} / {color_end}]\t "
don1 = f"[{color_cyan} - {color_end}]\t "
don2 = f"[{color_cyan} \ {color_end}]\t "
don3 = f"[{color_cyan} | {color_end}]\t "

don0 = "[" + color_cyan + "/".center(4) + color_end + "]\t "
don1 = "[" + color_cyan + "-".center(4) + color_end + "]\t "
don2 = "[" + color_cyan + "\\".center(4) + color_end + "]\t "
don3 = "[" + color_cyan + "|".center(4) + color_end + "]\t "

def main():
    for i in range(5):
        sys.stdout.write("\r" + don0)
        time.sleep(0.75)
        sys.stdout.flush()
        sys.stdout.write("\r" + don1)
        time.sleep(0.75)
        sys.stdout.flush()
        sys.stdout.write("\r" + don2)
        time.sleep(0.75)
        sys.stdout.flush()
        sys.stdout.write("\r" + don3)
        time.sleep(0.75)
        sys.stdout.write("\r")
        print(str_prefix_done + "Saved ")
    sys.exit()

if __name__ == "__main__":
    main()
