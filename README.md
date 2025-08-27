# Video İndirici

Bu basit Python betiği, bir YouTube videosunu belirtilen bir klasöre indirmek için **yt-dlp** kütüphanesini kullanır.

## -- Özellikler --
- Belirtilen URL'den videoyu indirir.

- İndirme dizini mevcut değilse otomatik olarak oluşturur.

- Video dosyası, video başlığı ve uzantısıyla kaydedilir.

- İndirme işlemi tamamlandığında veya bir hata oluştuğunda konsola bilgi mesajı yazdırır.

## -- Önkoşullar --
Bu betiği çalıştırmak için Python kurulu olmalıdır. Ayrıca, yt-dlp kütüphanesini kurmanız gerekmektedir.

## -- Kurulum --

Komut satırında aşağıdaki komutu çalıştırarak yt-dlp kütüphanesini kurun:

```
pip install yt-dlp
```

## -- Kullanım

Yukarıdaki kodu video_indirici.py gibi bir dosyaya kaydedin.

Dosyayı bir metin düzenleyici ile açın ve video_url ile indirme_klasoru değişkenlerini indirmek istediğiniz video URL'si ve kaydetmek istediğiniz klasör yolu ile güncelleyin.


## --- KULLANIMI ---

### İndirmek istediğiniz videonun URL'sini buraya yapıştırın

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Örnek URL

### Videonun kaydedileceği dizini buraya yazın
```
indirme_klasoru = "videolarim" # 'videolarim' klasörüne indirir
```
Terminalde veya komut isteminde, dosyanın bulunduğu dizine gidin ve betiği aşağıdaki komutla çalıştırın:

```
python video_indirici.py
```
Betiği çalıştırdıktan sonra, video belirtilen klasöre indirilecektir. İndirme işlemiyle ilgili bilgiler terminalde görüntülenecektir.
