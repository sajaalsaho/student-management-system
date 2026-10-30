# Konteynerleştirilmiş Öğrenci Yönetim Sistemi

## A-) Proje Tanımı ve Amacı
Bu proje, Modern Yazılım Mühendisliği – Bulut ve DevOps dersi kapsamında; 
küçük ölçekli ve temel fonksiyonlara sahip bir Öğrenci Yönetim Sistemi geliştirilmesini amaçlamaktadır.
Süreç, yazılım yaşam döngüsüne uygun olarak DevOps ve bulut yaklaşımlarıyla yönetilmekte; 
versiyon kontrolü, otomatik test, CI/CD pipeline, Docker ile konteynerleştirme ve bulut dağıtımı süreçleri uygulamalı olarak entegre edilmektedir.
## B-) Temel Fonksiyonlar
Sistemin barındırdığı temel fonksiyonlar şunlardır:

1-) **Öğrenci Kayıt ve Yönetimi:** Sisteme yeni öğrenci ekleme, mevcut öğrencileri listeleme ve silme.

2-) **Ders Tanımlama:** Sisteme yeni dersler tanımlama ve açma.

3-) **Not Girişi ve Hesaplama:** Öğrencilerin aldıkları derslere göre not girişi yapılması ve genel ortalamanın hesaplanması.

4-) **Raporlama:** Öğrenci listesini ve not dökümlerini görüntüleme.

## C-) Kullanılan Teknolojiler
* **Programlama Dili:** Python (Flask).
* **Veritabanı:** SQLite.
* **Versiyon Kontrolü:** Git & GitHub.
* **Proje Yönetimi (Agile):** GitHub Projects (Kanban Panosu).
* **Test Aracı:** Pytest (Otomatik Birim Testleri).
* **CI/CD:** GitHub Actions.
* **Konteynerleştirme:** Docker.
* **Bulut Dağıtımı :** Render / Railway (PaaS).


## D-) Kurulum ve Çalıştırma
```bash
git clone https://github.com/sajaalsaho/student-management-system.git
cd student-management-system
python -m venv venv
# Windows: venv\Scripts\Activate.ps1   |  Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Uygulama: http://127.0.0.1:5000

## E-) Test
```bash
pytest -v
```
## F-) Docker
```bash
docker build -t student-management-system .
docker run -p 5000:5000 student-management-system
```

## G-) Canlı Uygulama
(Hafta 06'da eklenecek)