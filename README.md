#README.md
#SITA AMIRA SYARIFAH
#NPM : 2206023023
PBP B

Tugas 3

1. Perbedaan antara form POST dan form GET dalam Django :
a) POST mengirimkan data/nilai secara langsung ke action tanpa menampilkannya di URL.
b) GET menampilkan data/nilai di URL yang dapat dilihat oleh semua pengguna, sebelum ditampung oleh action.
c) POST tidak memiliki batasan jumlah data yang dapat dikirimkan.
d) GET memiliki batasan maksimal karakter, yaitu 2047 karakter.
e) POST biasanya digunakan untuk mengirimkan data yang bersifat sensitif dan penting, contohnya password. Data tersebut biasanya akan diperbaharui atau dihapus dari server
f) GET cocok digunakan jika data bersifat publik dan ingin dtampilkan di URL, misalnya saat melakukan pencarian (data diambil dari server).
g) POST lebih aman karena dilindungi oleh token CSRF (Cross-Site-Request Forgery) untuk mencegah serangan CSRF dan data tidak terlihat di URL.
h) GET kurang aman karena datanya terlihat di URL.
i) POST digunakan untuk menerima semua request yang bisa mengubah server.
j) GET digunakan untuk mengubah data yang diterima dalam bentuk URL.
k) POST digunakan untuk data yang dapat diproses dan dimodifikasi.
l) GET digunakan untuk mengambil data yang tidak mempengaruhi server.

2. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah :
Umumnya, HTML dipakai untuk mengatur bagaimana suatu data ditampilkan seperti menampilkan konten pada browser, sedangkan XML dan JSON dipakai untuk menyimpan dan mengirim data. Perbedaan antara XML dan JSON terdapat pada formatnya. JSON menggunakan {} (kurung kurawal) dan lebih mudah dibaca. Adapun XML menggunakan start dan end tag seperti HTML, dan lebih aman dibandingkan JSON.

3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena representasi datanya yang lebih mudah dibaca oleh manusia dikarenakan strukturnya yang sederhana. JSON juga mendukung berbagai jenis data, seperti teks, angka, objek, etc. JSON juga cocok untuk penggunaan di aplikasi web yang memanfaatkan JavaScript dan AJAX (Asynchronous JavaScript and XML). Selain itu, JSON memiliki struktur yang ringan dan penguraian servernya mudah dilakukan oleh berbagai bahasa pemrograman khususnya JavaScript dan memiliki overhead yang lebih rendah dibandingkan XML.


4. Cara saya dalam mengimplementasikan checklist tugas secara step by step adalah :
- Pertama, membuat template dasar pada file base.html -> mengubah setting.py sehingga base.html terdeteksi sebagai template dengan menambahkan kode 
add 'DIRS': [BASE_DIR / 'templates'],. di Templates -> sesuaikan konten yang terdapat di main.html dengan template yang terdapat di base.html
- Kedua, membuat file forms.py yang dapat menerima data produk baru dengan modelnya Product dan fieldsnya name, amount, price, dan description -> di file views.py yang terdapat pada direktori main, buat function create_product dengan request POST, agar data otomatis tersimpan saat mensubmit form.
- Ketiga, import HttpResponse dan serializers.
HTML: Fungsi show_main yang sebelumnya, saya menambahkan products pada context yang berisi semua object yang diinput pada form. Untuk mengambil semua objectnya, saya menggunakan Product.objects.all().
XML: membuat fungsi show_xml yang dapat menerima request dan akan mereturn HttpResponse dengan parameter seperti berikut:
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
JSON (show_json): sama seperti xml, hanya saja pada bagian serializers dan content_type diubah menjadi json.
JSON dan XML by id: mirip seperti tanpa id, tetapi object yang dicari difilter berdasarkan id. Kodenya hanya berbeda di bagian data = Product.objects.filter(pk=id).
- Terakhir, membuat routing URL untuk masing masing views dengan cara mengimport 4 function yang sebelumnya telah dibuat serta menambahkan 4 path url (html sudah dikerjakan di tugas 2) pada file urls.py dibagian urlpatterns untuk keempat fungsi yang baru yang ditambahkan pada views.py sebelumnya.
















=============================================================================

Tugas 2
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

3. Virtual environment sangat disarankan dalam pengembangan aplikasi berbasis Django dan pengembangan perangkat lunak pada umumnya. Alasannya adalah :
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

