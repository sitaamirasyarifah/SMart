#README.md
#SITA AMIRA SYARIFAH
#NPM : 2206023023
PBP B

Link Aplikasi Adaptable : https://smart.adaptable.app/main

1. Cara saya mengimplementasikan checklist tersebut adalah :
   - Membuat sebuah proyek Django baru :
     Pertama saya membuat repository baru di Github dengan nama sesuai yang saya inginkan, yaitu "SMart" untuk proyek baru dan melakukan git clone melalui command prompt. Setelah cloning dan muncul di direktori lokal, saya membuat file "requirements.txt" serta menginstal Django untuk deployment aplikasi.
     
   - Membuat aplikasi dengan nama main pada proyek tersebut :
     Menjalankan perintah python manage.py startapp main pada direktori "SMart" menggunakan command prompt.
     
   - Melakukan Routing pada proyek
     Pada file settings.py di direktori proyek "SMart", tambahkan "main" pada bagian "INSTALLED APPS" agar main bisa dijalankan.

   - Membuat Model "Item"
     Membuka file "models.py" dan membuat class Item serta menambah ketiga item yaitu name (CharField), amount (IntegerField) dan description (TextField) sesuai ketentuan tugas.

   - Membuat fungsi pada views.py untuk mengembalikan ke dalam template HTML yang menampilkan nama aplikasi serta nama dan kelas
     Menambahkan fungsi "show_main" pada files "views.py" yang me-render "main.html". File "main.html" diisi dengan judul aplikasi, nama, kelas, NPM sesuai format. Dapat disesuaikan dengan "context" yang ada di fungsi "show_main" dalam file "views.py"
   
   - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
     Mengimport path dari django.urls untuk mendefinisikan pola URL dan menggunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.

   - Melakukan deployment ke Adaptable
     Mengakses adaptable.io kemudian create new app, connect dengan repository "SMart" yang sudah tersedia di GitHub, kemudian memilih PythonApp template dan PostgreSQL. Lalu sesuaikan versi python sesuai yang kita miliki dan menambahkan command "python manage.py migrate && gunicorn SMart.wsgi" lalu isi nama aplikasi sesuai yang diinginkan, dan aktifkan HTTP Listener on PORT. Terakhir, tinggal menunggu deployment aplikasi selesai.

2. Bagan request client ke web aplikasi berbasis Django
   ![WhatsApp Image 2023-09-13 at 07 38 41](https://github.com/sitaamirasyarifah/SMart/assets/122429830/9ea8f0b2-4028-4fa9-aa5b-25b925fe1bc0)



4. Virtual environment sangat disarankan dalam pengembangan aplikasi berbasis Django dan pengembangan perangkat lunak pada umumnya. Alasannya adalah :
- Virtual environment memungkinkan kita untuk membuat lingkungan isolasi yang independen untuk setiap proyek. Ini berarti setiap proyek dapat memiliki dependensi yang berbeda tanpa menganggu satu sama lain. Misalnya, proyek A mungkin memerlukan versi Django tertentu, sedangkan proyek B memerlukan versi yang berbeda. Dengan virtual environment, kita dapat memenuhi persyaratan khusus setiap proyek tanpa konflik. 
- Dengan virtual environment, kita dapat mengelola dependensi proyek secara lebih efektif. Kita dapat menginstall, menghapus, dan mengganti dependensi proyek tanpa memengaruhi proyek lainnya.
- Ketika bekerja dalam tim, virtual environment memungkinkan semua anggota tim menggunakan lingkungan yang serupa, sehingga mengurangi masalah terkait dengan perbedaan konfigurasi.
Meskipun sangat disarankan untuk menggunakan virtual environment saat mengembangkan aplikasi Django, secara teknis kita dapat membuat aplikasi web Django tanpa virtual environment. Namun, hal ini tidak disarankan karena akan menimbulkan banyak masalah yang dapat memengaruhi stabilitas dan keamanan sistem, serta dapat menyulitkan pengelolaan dependensi proyek yang berbeda. Oleh karena itu, sangat dianjurkan untuk selalu menggunakan virtual environment dalam pengembangan aplikasi berbasis Django dan proyek Python lainnya. 

4. MVC, MVT, dan MVVM adalah konsep dalam pengembangan aplikasi web yang memiliki kesamaan dengan adanya "Model" dan "View," tetapi memiliki perbedaan dalam bagaimana Model, View, dan komponen ketiga (Controller, Template, dan ViewModel) berinteraksi.

Secara umum, "Model" digunakan sebagai tempat penyimpanan data, sementara "View" bertanggung jawab untuk menampilkan informasi kepada pengguna.

Perbedaan utama antara ketiga konsep ini terletak pada peran komponen ketiga:

- MVC (Model-View-Controller): Menggunakan Controller sebagai penghubung antara Model dan View. Controller mengurus pembaruan Model dan View ketika terjadi perubahan.

- MVT (Model-View-Template): Bergantung pada Template untuk mengatur tampilan yang umumnya dalam bentuk HTML. Peran Controller dilakukan oleh framework web itu sendiri.

- MVVM (Model-View-ViewModel): Memiliki ViewModel yang bertugas menampilkan data kepada pengguna, sementara View digunakan untuk menyimpan cara menampilkan data dan merespons interaksi pengguna. Konsep MVVM lebih sederhana dibandingkan dengan MVC dan MVT.

