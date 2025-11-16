import os
import sys
import time
import random

GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def typewrite(text, delay=0.02):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fast_write(text, delay=0.001):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain(lines=25, width=70):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(width))
        fast_write(GREEN + line + RESET, delay=0.0003)

def fake_database_dump():
    typewrite(CYAN + "\n[*] CONNECTING TO DATABASE SERVER..." + RESET)
    time.sleep(1)

    db_tables = ["users", "passwords", "logs", "transactions", "sessions", "tokens"]
    for table in db_tables:
        typewrite(f"[+] Extracting table: {table} ...")
        for i in range(10):
            fake_data = ''.join(random.choice("abcdef1234567890") for _ in range(32))
            fast_write(GREEN + f"    row_{i}: {fake_data}" + RESET, delay=0.001)
        time.sleep(0.3)
    typewrite(GREEN + "[✓] DATABASE EXTRACTED SUCCESSFULLY.\n" + RESET)

def fake_ddos_attack():
    typewrite(RED + "[!] INITIATING DISTRIBUTED ATTACK..." + RESET)
    time.sleep(1)

    for i in range(1, 101):
        fake_ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
        fast_write(YELLOW + f"[DDoS] Flooding {fake_ip}: packet {i}/100" + RESET, delay=0.0008)
        time.sleep(0.02)

    typewrite(GREEN + "[✓] ATTACK COMPLETED (simulation)\n" + RESET)

def fake_access_granted():
    typewrite(GREEN + "\n=== ACCESS LEVEL 7 GRANTED ===" + RESET)
    typewrite(CYAN + "[*] Launching Admin Control Panel..." + RESET)
    time.sleep(1)

def main():
    os.system("clear")
    typewrite(GREEN + "BOOTING HACKER TERMINAL v3.0..." + RESET, delay=0.03)
    time.sleep(1)
    matrix_rain()

    fake_database_dump()
    fake_ddos_attack()
    fake_access_granted()

    typewrite(RED + "\n[!] NOTE: This is only a simulation. No real hacking is happening." + RESET)

if __name__ == "__main__":
    main()
