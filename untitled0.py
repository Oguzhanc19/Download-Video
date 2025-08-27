import yt_dlp
import os

def video_indir(url, indirme_dizini="."):
    """
    Belirtilen URL'den videoyu, belirtilen dizine indirir.

    Args:
        url (str): İndirilecek videonun URL'si.
        indirme_dizini (str): Videonun kaydedileceği dizin yolu.
    """
    try:
        # İndirme dizini mevcut değilse oluştur.
        if not os.path.exists(indirme_dizini):
            os.makedirs(indirme_dizini)

        # Dosya adını ve yolunu birleştir.
        # '%(title)s.%(ext)s' ile dosya adı video başlığı ve uzantısı olur.
        dosya_yolu = os.path.join(indirme_dizini, '%(title)s.%(ext)s')

        # yt-dlp ayarlarını tanımla.
        ydl_opts = {
            'outtmpl': dosya_yolu,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("Video başarıyla indirildi!")
        print(f"Konum: {os.path.abspath(indirme_dizini)}")
        
    except Exception as e:
        print(f"Video indirilirken bir hata oluştu: {e}")

# --- KULLANIMI ---

# İndirmek istediğiniz videonun URL'sini buraya yapıştırın
video_url = input("URL Gir:")

# Videonun kaydedileceği dizini buraya yazın
# Örneğin, "videolarim" adında bir klasöre kaydetmek için
indirme_klasoru = "videolarim"

# Fonksiyonu çağırarak indirme işlemini başlatın
video_indir(video_url, indirme_klasoru)