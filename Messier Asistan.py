import datetime
import webbrowser
import urllib.parse # Güvenlik için eklendi

def selamla():
  print("Merhaba! Sana nasıl yardımcı olabilirim?")

def zaman_sor():
  simdi = datetime.datetime.now()
  print(f"Şu anki zaman: {simdi.strftime('%H:%M:%S')}")

def duckduckgo(arama_terimi):
  url = "https://duckduckgo.com/?q=" + urllib.parse.quote(arama_terimi) # Güvenlik için URL kodlaması eklendi
  webbrowser.open(url)

def cikis():
  print("Görüşmek üzere!")
  exit()
selamla()
while True:
  komut = input("Komutunuzu girin (zaman, arama, çıkış, yapayzeka): ").lower()

  if komut == "selam":
    selamla()
  elif komut == "zaman":
    zaman_sor()
  elif komut.startswith("arama"):
    arama_terimi = komut[6:]
    duckduckgo(arama_terimi)
  elif komut.startswith("yapayzeka"):
    webbrowser.open("https://poe.com/Messier_AI")
  elif komut == "çıkış":
    cikis()
  else:
    print("Geçersiz komut.")