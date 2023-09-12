#README.md
#SITA AMIRA SYARIFAH
#NPM : 2206023023
PBP B

1. Cara saya mengimplementasikan checklist tersebut adalah :
a) Membuat sebuah proyek Django baru :
   Pertama saya membuat repository baru di Github dengan nama sesuai yang saya inginkan, yaitu "SMart" untuk proyek baru dan melakukan git clone melalui command prompt. Setelah cloning dan muncul di direktori lokal, saya membuat file "requirements.txt" serta menginstal Django untuk deployment aplikasi.
b) Membuat aplikasi dengan nama main pada proyek tersebut :
   Menjalankan perintah python manage.py startapp main pada direktori "SMart" menggunakan command prompt.
c) Melakukan Routing pada proyek
   Pada file settings.py di direktori proyek "SMart", tambahkan "main" pada bagian "INSTALLED APPS" agar main bisa dijalankan.
d) Membuat Model "Item"
   Membuka file "models.py" dan membuat class Item serta menambah ketiga item yaitu name (CharField), amount (IntegerField) dan description (TextField) sesuai ketentuan tugas.
e) Membuat fungsi pada views.py untuk mengembalikan ke dalam template HTML yang menampilkan nama aplikasi serta nama dan kelas
   Menambahkan fungsi "show_main" pada files "views.py" yang me-render "main.html". File "main.html" diisi dengan judul aplikasi, nama, kelas, NPM sesuai format. Dapat disesuaikan dengan "context" yang ada di fungsi "show_main" dalam file "views.py"
f) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
   Mengimport path dari django.urls untuk mendefinisikan pola URL dan menggunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.