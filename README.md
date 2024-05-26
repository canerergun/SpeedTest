# Hız Testi Betiği

Bu betik, internet bağlantınızın indirme ve yükleme hızlarını, ve ping süresini ölçmek için `speedtest` modülünü kullanır. Konumunuza en uygun sunucuyu bulur ve hız testini gerçekleştirerek sonuçları yazdırır.

## Kullanım

Betiği çalıştırmak için `speedtest-cli` modülünün yüklü olduğundan emin olun. Bu modülü pip kullanarak yükleyebilirsiniz:

```sh
pip install speedtest-cli
```

Betik bir dosyaya, örneğin `hiz_testi.py` dosyasına kaydedin ve Python ile çalıştırın:

```sh
python hiz_testi.py
```

## Betik Açıklaması

1. **`speedtest` modülünü içe aktarın:**

    ```python
    import speedtest
    ```

2. **Bir Speedtest nesnesi oluşturun:**

    ```python
    st = speedtest.Speedtest()
    ```

3. **Sunucu listesini yükleyin:**

    ```python
    print("Sunucu listesi yükleniyor...")
    st.get_servers()
    ```

4. **Konumunuza en uygun sunucuyu bulun:**

    ```python
    print("En uygun sunucu aranıyor...")
    best_server = st.get_best_server()
    ```

5. **En iyi sunucu hakkında bilgi yazdırın:**

    ```python
    print("\nSunucu Bilgileri:")
    print(f"Ülke: {best_server['country']}")
    print(f"Şehir: {best_server['name']}")
    print(f"Sağlayıcı: {best_server['sponsor']}")
    print(f"Sunucu: {best_server['host']}")
    print("-"*45)
    ```

6. **İndirme hızını ölçün ve yazdırın:**

    ```python
    print("\nİndirme hızı test ediliyor...")
    download_speed = st.download() / 1024 / 1024  # Mbps cinsinden
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    ```

7. **Yükleme hızını ölçün ve yazdırın:**

    ```python
    print("\nYükleme hızı test ediliyor...")
    upload_speed = st.upload() / 1024 / 1024  # Mbps cinsinden
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    ```

8. **Ping süresini ölçün ve yazdırın:**

    ```python
    print("\nPing süresi ölçülüyor...")
    ping = st.results.ping
    print(f"Ping: {ping} ms")
    ```

## Notlar

- Betiği çalıştırırken doğru sonuçlar almak için sabit bir internet bağlantısına sahip olun.
- Betik, mevcut konumunuza ve ağ koşullarına göre en uygun sunucuyu otomatik olarak seçer.
- İndirme ve yükleme hızları Mbps (Megabit/saniye) cinsinden ölçülür.

## Lisans

Bu betik MIT Lisansı altında lisanslanmıştır. Bu lisansın şartlarına uygun olarak bu betiği kullanmakta, değiştirmekte ve dağıtmakta özgürsünüz.
