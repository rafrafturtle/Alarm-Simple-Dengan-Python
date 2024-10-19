import datetime
import time
import pygame

def status_timer(waktu_bangun):
    print(f"Alarm diset untuk waktu {waktu_bangun}")
    lagu = "music.mp3"
    status_nyala = True

    while status_nyala:
        waktu_sekarang = datetime.datetime.now().strftime("%H:%M:%S")
        print(waktu_sekarang)
        time.sleep(1)

        if waktu_sekarang == waktu_bangun:
            print("Saatnya Bangun 😮😮")
            pygame.mixer.init()
            pygame.mixer.music.load(lagu)
            pygame.mixer.music.play(-1)
            
            while True:
                konfirmasi = input("Ketik 'bangun' Untuk Berhenti : ").lower()
                if konfirmasi == "bangun":
                    status_nyala = False
                    print("Selamat memulai Hari 😁")
                    break

if __name__ == "__main__":
    waktu_bangun = input("Masukkan waktu untuk alarm (JJ:MM:DD) : ")
    status_timer(waktu_bangun)