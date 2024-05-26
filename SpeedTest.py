import speedtest

def main():
    # Speedtest objesini oluştur
    st = speedtest.Speedtest()
    
    # Sunucu listesini yükle
    print("Sunucu listesi yükleniyor...")
    st.get_servers()

    # En iyi sunucuyu bul
    print("En uygun sunucu aranıyor...")
    best_server = st.get_best_server()

    # En iyi sunucunun bilgileri
    print("\nSunucu Bilgileri:")
    print(f"Ülke: {best_server['country']}")
    print(f"Şehir: {best_server['name']}")
    print(f"Sağlayıcı: {best_server['sponsor']}")
    print(f"Sunucu: {best_server['host']}")
    print("-"*45)

    # İndirme hızını ölç
    print("\nİndirme hızı test ediliyor...")
    download_speed = st.download() / 1024 / 1024  # Mbps cinsinden
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")

    # Yükleme hızını ölç
    print("\nYükleme hızı test ediliyor...")
    upload_speed = st.upload() / 1024 / 1024  # Mbps cinsinden
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")

    # Ping süresini ölç
    print("\nPing süresi ölçülüyor...")
    ping = st.results.ping
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    main()
