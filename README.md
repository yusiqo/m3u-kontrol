
# M3U Kanal Doğrulayıcı

Bu Python scripti, bir M3U oynatma listesindeki kanalları test eder ve çalışmayanları filtreler. Çalışan kanallar daha sonra yeni bir M3U dosyasına kaydedilir. Bu araç, oynatma listesinde yalnızca aktif kanalların bulunmasını sağlamak isteyen IPTV kullanıcıları için özellikle yararlıdır.

## Özellikler

- **URL Testi:** M3U dosyasındaki her kanalın URL'sinin erişilebilir olup olmadığını doğrular.
- **Günlükleme:** Her URL'nin durumunu kaydeder ve başarısız bağlantılar hakkında ayrıntılı bilgi sağlar.
- **Çıktı Üretimi:** Yalnızca çalışan kanallarla yeni bir M3U dosyası oluşturur.

## Gereksinimler

- Python 3.6 veya üzeri
- `requests` kütüphanesi

## Kurulum

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/yusiqo/m3u-kontrol.git
   cd m3u-kontrol
   ```

2. **Bağımlılıkları Yükleyin:**
   Gerekli bağımlılıkları pip kullanarak yükleyebilirsiniz:
   ```bash
   pip install -r requirements.txt
   ```

3. **Scripti Yürütülebilir Hale Getirin (İsteğe Bağlı):**
   Unix tabanlı sistemlerde (Linux/MacOS), scripti yürütülebilir hale getirebilirsiniz:
   ```bash
   chmod +x kontrol.py
   ```

## Kullanım

Scripti aşağıdaki komutla çalıştırabilirsiniz:

```bash
python3 kontrol.py -i "input.m3u" -o "output.m3u"
```

### Argümanlar

- `-i, --input`: **(Zorunlu)** Girdi M3U dosyasının yolu.
- `-o, --output`: **(Zorunlu)** Çıktı M3U dosyasının yolu; çalışan kanallar bu dosyaya kaydedilecektir.

### Örnek

```bash
python3 kontrol.py -i "playlistim.m3u" -o "calisan_kanallar.m3u"
```

Bu örnekte:
- `"playlistim.m3u"` orijinal kanal listesini içeren girdi dosyasıdır.
- `"calisan_kanallar.m3u"` ise yalnızca şu anda çalışan kanalları içerecek olan çıktı dosyasıdır.

## Günlükleme

Script, işlem sürecinin ayrıntılı günlüklerini sağlamak için `logging` modülünü kullanır. Varsayılan olarak, günlükler konsola yazdırılır ve şunları gösterir:
- İşlem aşamaları hakkında bilgi.
- Erişilemeyen URL'ler gibi karşılaşılan hatalar.

### Örnek Günlük Çıktısı

```
2024-08-11 12:00:00 - INFO - input.m3u dosyası işleniyor...
2024-08-11 12:00:10 - ERROR - URL çalışmıyor: http://example.com/stream.m3u8, Hata: HTTPConnectionPool(host='example.com', port=80): Max retries exceeded with url: /stream.m3u8 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x...>: Failed to establish a new connection: [Errno 111] Connection refused'))
2024-08-11 12:00:20 - INFO - Toplam 5 kanal çalışıyor.
2024-08-11 12:00:30 - INFO - Çalışan kanallar output.m3u dosyasına kaydedildi.
2024-08-11 12:00:40 - INFO - İşlem tamamlandı.
```

## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Bu scripti geliştirmek veya yeni özellikler eklemek isterseniz, depoyu forkladıktan sonra bir pull request gönderebilirsiniz.

1. **Depoyu Forklayın**
2. **Yeni bir dal oluşturun**: `git checkout -b ozellik-adi`
3. **Değişikliklerinizi yapın**
4. **Değişikliklerinizi commit edin**: `git commit -m 'Özellik eklendi'`
5. **Dala push edin**: `git push origin ozellik-adi`
6. **Pull request gönderin**

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
