#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import math

try:
    os.mkdir('/sdcard/ALI')
except Exception:
    pass


RESET  = "\033[0m"
RED    = "\033[1;31m"
GREEN  = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE   = "\033[1;94m"
PURPLE = "\033[1;35m"
CYAN   = "\033[1;36m"
WHITE  = "\033[1;37m"
GREY   = "\033[90m"


def __rgb__(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def __rainbow__(t):
    r = int((math.sin(t) * 127) + 128)
    g = int((math.sin(t + 2.094) * 127) + 128)
    b = int((math.sin(t + 4.188) * 127) + 128)
    return r, g, b


def show_box():
    __logo = r"""
_____________________          ____  ___
\_   _____/\______   \         \   \/  /
 |    __)   |    |  _/  ______  \     /
 |     \    |    |   \ /_____/  /     \
 \___  /    |______  /         /___/\  \
     \/            \/                \_/
""".strip("\n").splitlines()

    __info = [
        "",
        "OWNER   : M.Ali",
        "Tool    : FILE-CREATE",
        "Version : Personal",
        "Contact : 03xxxxxxx",
        ""
    ]

    __left_width  = max(len(line) for line in __logo) + 2
    __right_width = max(len(line) for line in __info) + 2
    __total_width = __left_width + __right_width + 5

    __r, __g, __b    = __rainbow__(time.time() * 2)
    __r2, __g2, __b2 = __rainbow__(time.time() * 2 + 1.5)

    __top    = __rgb__(__r, __g, __b, "╔") + __rgb__(__r, __g, __b, "═" * __total_width) + __rgb__(__r, __g, __b, "╗")
    __bottom = __rgb__(__r2, __g2, __b2, "╚") + __rgb__(__r2, __g2, __b2, "═" * __total_width) + __rgb__(__r2, __g2, __b2, "╝")

    output = __top + "\n"

    for i in range(max(len(__logo), len(__info))):
        left  = (__logo[i] if i < len(__logo) else "").ljust(__left_width)
        right = (__info[i] if i < len(__info) else "").ljust(__right_width)

        lc1 = __rainbow__(time.time() * 3 + i * 0.3)
        lc2 = __rainbow__(time.time() * 3 + i * 0.3 + 1)
        vc1 = __rainbow__(time.time() * 4 + i * 0.2)
        vc2 = __rainbow__(time.time() * 4 + i * 0.2 + 0.5)

        output += (
            f"{__rgb__(*vc1, '║')} "
            f"{__rgb__(*lc1, left)}   "
            f"{__rgb__(*lc2, right)} "
            f"{__rgb__(*vc2, '║')}\n"
        )

    output += __bottom
    return output


def linex():
    r, g, b = __rainbow__(time.time() * 2)
    print(__rgb__(r, g, b, "═" * 70))


def clear():
    os.system('clear')
    print(show_box())


def main_menu():
    while True:
        clear()
        print("  \033[1;97m[\033[1;96m1\033[1;97m] CLONING MENU")
        print("  \033[1;97m[\033[1;96m2\033[1;97m] FILE MENU")
        print("  \033[1;97m[\033[1;96m3\033[1;97m] Exit")
        linex()
        choice = input("  \033[1;92m➤ Select Option : \033[0m").strip()

        if choice == "1":
            clear()
            print("\033[1;93m[+] Starting Cloning Menu...\033[0m")
            time.sleep(5)
            try:
                import FBX
                FBX.main()
            except Exception as e:
                print(f"\n  \033[1;91m[!] Error: {e}\033[0m")
            input("\n  \033[1;97mPress Enter to return...\033[0m")

        elif choice == "2":
            clear()
            print("  \033[1;93m[+] Starting File Create Menu...\033[0m")
            time.sleep(5)
            try:
                import FCX
                FCX.main()
            except Exception as e:
                print(f"\n  \033[1;91m[!] Error: {e}\033[0m")
            input("\n  \033[1;97mPress Enter to return...\033[0m")

        elif choice == "3":
            print("\n  \033[1;92m[✓] Good Bye — M.Ali\033[0m\n")
            sys.exit(0)

        else:
            print("\n  \033[1;91m[!] Invalid option\033[0m")
            time.sleep(1)


def main():
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n  \033[1;91m[!] Stopped by user\033[0m\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
