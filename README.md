<div align="center">
  <h1>📥 Video Downloader Tool</h1>
  <p><i>Automated Media Extraction using yt-dlp<br>yt-dlp Kullanarak Otomatik Medya İndirme Aracı</i></p>
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
</div>

<br>

## 🇬🇧 English

A highly efficient Python utility designed to download videos from a vast array of online platforms. Instead of relying on outdated libraries like `pytube`, this project leverages the powerful **`yt-dlp`** engine.

### 🧠 Implementation Details
- **Dynamic File Naming**: Uses `yt-dlp`'s outtmpl syntax (`%(title)s.%(ext)s`) to automatically parse the video's original title and best extension format, saving the file cleanly.
- **Directory Management**: Implements `os.path.exists()` and `os.makedirs()` to dynamically create the target download folder if it doesn't exist, preventing path errors.
- **Exception Handling**: Wrapped in `try-except` blocks to ensure the program doesn't crash upon encountering a dead URL or network timeout.

---

## 🇹🇷 Türkçe

Birçok çevrimiçi platformdan video indirmek için tasarlanmış yüksek verimli bir Python aracıdır. Sürekli bozulan `pytube` gibi eski kütüphaneler yerine, çok daha güçlü ve güncel olan **`yt-dlp`** motorunu kullanır.

### 🧠 Uygulama Detayları
- **Dinamik Dosya İsimlendirme**: Videonun orijinal başlığını ve uzantısını otomatik olarak çekmek için `yt-dlp`nin `%(title)s.%(ext)s` formatını kullanır, böylece dosyalar isimsiz veya karmaşık adlarla kaydedilmez.
- **Dizin (Klasör) Yönetimi**: `os.path.exists()` ve `os.makedirs()` kullanarak hedeflenen indirme klasörü yoksa otomatik olarak oluşturur; bu sayede yol (path) hatalarının önüne geçilir.
- **Hata Yakalama (Exception Handling)**: Hatalı bir link girildiğinde veya internet koptuğunda programın çökmesini engellemek için tüm işlemler `try-except` blokları içine alınmıştır.
