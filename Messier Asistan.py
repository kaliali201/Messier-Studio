
import tkinter as tk
import datetime
import webbrowser
import urllib.parse
import time
from playsound import playsound
file = r"C:\Users\Kaan\Desktop\projeler\Galaxy-Note-4-Melody.mp3"
def selamla():
    mesaj_alani.insert(tk.END, "Merhaba! Sana nasıl yardımcı olabilirim?\n")

def zaman_sor():
    simdi = datetime.datetime.now()
    zaman_metni = f"Şu anki zaman: {simdi.strftime('%H:%M:%S')}\n"
    mesaj_alani.config(state=tk.NORMAL) # Yazma yeteneğini etkinleştir
    mesaj_alani.insert(tk.END, zaman_metni)
    mesaj_alani.config(state=tk.DISABLED) # Yazma yeteneğini devre dışı bırak


def duckduckgo(arama_terimi):
    url = "https://duckduckgo.com/?q=" + urllib.parse.quote(arama_terimi)
    try:
        webbrowser.open(url)
        mesaj_alani.insert(tk.END, f"DuckDuckGo'da '{arama_terimi}' için arama yapılıyor...\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: {e}\n")


def poe_ac():
    try:
        webbrowser.open("https://poe.com/Messier_AI")
        mesaj_alani.insert(tk.END, "Messier_AI Poe sayfasına yönlendiriliyorsunuz...\n")
    except Exception as e:
        mesaj_alani.insert(tk.END, f"Hata: {e}\n")


def komut_islec(event=None):
    komut = giris_alani.get().lower()
    giris_alani.delete(0, tk.END) # Giriş alanını temizle

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
        saniye = int(komut[12:]) # Hata fırlatabilir!
        dakika = saniye * 60       
        time.sleep(dakika)         
        playsound(file) # Hata fırlatabilir!
    else:
        mesaj_alani.insert(tk.END, "Geçersiz komut.\n")


# Tkinter penceresi oluşturma
pencere = tk.Tk()
pencere.title("Messier Asistanım")

# Etiketler ve giriş alanı
etiket = tk.Label(pencere, text="Komutunuzu girin:")
etiket.pack(pady=5)

giris_alani = tk.Entry(pencere)
giris_alani.pack(pady=5)
giris_alani.bind("<Return>", komut_islec) # Enter tuşuna basıldığında komutu çalıştır

# Komut butonu
komut_butonu = tk.Button(pencere, text="Gönder", command=komut_islec)
komut_butonu.pack(pady=5)

# Mesaj alanı
mesaj_alani = tk.Text(pencere, height=10, width=40)
mesaj_alani.pack(pady=5)
mesaj_alani.config(state=tk.DISABLED) # Kullanıcının doğrudan yazmasını engelle


pencere.mainloop()
