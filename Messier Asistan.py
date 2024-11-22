import tkinter as tk
import datetime
import webbrowser
import urllib.parse
import time
import os
from playsound import playsound

default_sound_file = r"Galaxy-Note-4-Melody.mp3"

if not os.path.exists(default_sound_file):
    uyari_mesaji = "Uyarı: Varsayılan ses dosyası bulunamadı. Zamanlayıcı sesi çalınmayacak.\n"
else:
    uyari_mesaji = ""


def selamla():
    mesaj_alani.insert(tk.END, "Merhaba! Sana nasıl yardımcı olabilirim?\n")

def zaman_sor():
    simdi = datetime.datetime.now()
    zaman_metni = f"Şu anki zaman: {simdi.strftime('%H:%M:%S')}\n"
    mesaj_alani.config(state=tk.NORMAL)
    mesaj_alani.insert(tk.END, zaman_metni)
    mesaj_alani.config(state=tk.DISABLED)


def duckduckgo(arama_terimi):
    url = "https://duckduckgo.com/?q=" + urllib.parse.quote(arama_terimi)
    try:
        webbrowser.open(url)
        mesaj_alani.insert(tk.END, f"DuckDuckGo'da '{arama_terimi}' için arama yapılıyor...\n")
    except webbrowser.Error as e:
        mesaj_alani.insert(tk.END, f"Hata: DuckDuckGo açılamadı: {e}\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: Beklenmedik bir hata oluştu: {e}\n")


def poe_ac():
    try:
        webbrowser.open("https://poe.com/Messier_AI")
        mesaj_alani.insert(tk.END, "Messier_AI Poe sayfasına yönlendiriliyorsunuz...\n")
    except webbrowser.Error as e:
        mesaj_alani.insert(tk.END, f"Hata: Poe sayfası açılamadı: {e}\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: Beklenmedik bir hata oluştu: {e}\n")


def zamanlayici(dakika):
    try:
        dakika_sn = int(dakika) * 60
        if dakika_sn <= 0:
            mesaj_alani.insert(tk.END, "Geçersiz süre. Lütfen pozitif bir sayı girin.\n")
            return

        time.sleep(dakika_sn)
        if os.path.exists(default_sound_file):
            try:
                playsound(default_sound_file)
            except playsound.PlaysoundException as e:
                mesaj_alani.insert(tk.END, f"Hata: Ses dosyası çalınamadı: {e}\n")
            except Exception as e:
                mesaj_alani.insert(tk.END, f"Hata: Ses dosyası çalınırken beklenmedik bir hata oluştu: {e}\n")
        mesaj_alani.insert(tk.END, f"{dakika} dakikalık zamanlayıcı tamamlandı!\n")
    except ValueError:
        mesaj_alani.insert(tk.END, "Geçersiz süre. Lütfen bir sayı girin.\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: Zamanlayıcıda beklenmedik bir hata oluştu: {e}\n")


def komut_islec(event=None):
    komut = giris_alani.get().lower()
    giris_alani.delete(0, tk.END)

    try:
        if komut == "selam":
            selamla()
        elif komut == "zaman":
            zaman_sor()
        elif komut.startswith("arama"):
            arama_terimi = komut[6:]
            duckduckgo(arama_terimi)
        elif komut == "yapayzeka" or komut == "messier ai":
            poe_ac()
        elif komut == "çıkış":
            pencere.destroy()
        elif komut.startswith("zamanlayıcı"):
            try:
                dakika = komut[11:]
                zamanlayici(dakika)
            except IndexError:
                mesaj_alani.insert(tk.END, "Lütfen zamanlayıcı süresini belirtin (örneğin: zamanlayıcı 5).\n")
        else:
            mesaj_alani.insert(tk.END, "Geçersiz komut.\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: Komut işlenirken beklenmedik bir hata oluştu: {e}\n")


pencere = tk.Tk()
pencere.title("Messier Asistanım")

etiket = tk.Label(pencere, text="Komutunuzu girin:")
etiket.pack(pady=5)

giris_alani = tk.Entry(pencere)
giris_alani.pack(pady=5)
giris_alani.bind("<Return>", komut_islec)

komut_butonu = tk.Button(pencere, text="Gönder", command=komut_islec)
komut_butonu.pack(pady=5)

mesaj_alani = tk.Text(pencere, height=10, width=40)
mesaj_alani.pack(pady=5)
mesaj_alani.config(state=tk.DISABLED)

mesaj_alani.config(state=tk.NORMAL)
mesaj_alani.insert(tk.END, uyari_mesaji)
mesaj_alani.config(state=tk.DISABLED)

pencere.mainloop()
