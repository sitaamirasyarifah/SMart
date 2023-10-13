#README.md
#SITA AMIRA SYARIFAH
#NPM : 2206023023
PBP B

Tugas 6
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Jawab :
- Synchronus programming
  Task akan dieksekusi secara satu persatu sesuai urutan dan prioritas task. Sehingga beberapa task tidak dapat dieksekusi secara bersamaan.
  Karena task dieksekusi satu persatu, maka waktu yang diperlukan untuk menyelesaikan semua task biasanya lebih lama.

- Asynchronus programming
  Tidak terikat pada I/O protocol, sehingga proses eksekusi program dilakukan secara independent dan dapat dilakukan secara bersamaan tanpa harus menunggu tugas sebelumnya selesai.
  Waktu total yang diperlukan untuk menyelesaikan task lebih sedikit.

2. Dalam penggunaan JavaScript dan AJAX, paradigma event-driven programming diterapkan. Paradigma ini mengacu pada cara program dijalankan berdasarkan event yang terjadi, baik itu dipicu oleh pengguna atau sistem. Sebagai contoh, saat tombol dengan ID "button_add" pada formulir AJAX ditekan, maka fungsi "addProduct" akan segera dieksekusi. Penerapannya dalam tugas ini, yaitu pada saat button dengan id button add (button add produk yang ada di dalam AJAX saat ingin submit form) diklik, akan langsung menjalankan function addProduct.
   Berikut kodenya:
- document.getElementById("button_add").onclick = addProduct

3.Penerapan asynchronous programming pada AJAX melibatkan beberapa aspek penting:
- Fungsi async dan await: Fungsi async digunakan untuk menandai sebuah fungsi sebagai fungsi yang dapat mengembalikan nilai secara asinkron, sementara fungsi await digunakan untuk menunggu hasil dari fungsi async. Ini memungkinkan tugas-tugas asinkron untuk berjalan tanpa menghentikan eksekusi program.
- Callback functions: Ini adalah fungsi yang akan dipanggil ketika permintaan AJAX selesai. Mereka memungkinkan Anda untuk mengatasi tugas-tugas yang harus dijalankan setelah permintaan AJAX selesai secara asinkron.
- XMLHttpRequest atau fetch: Dua opsi untuk membuat permintaan HTTP asinkron dalam JavaScript. Mereka memungkinkan JavaScript untuk terus menjalankan kode lain tanpa harus menunggu hasil permintaan.
- Penerapan asynchronous programming pada AJAX memungkinkan pemrosesan permintaan ke server secara asinkron, sehingga membuat antarmuka lebih responsif dan interaktif.

4. Dalam hal perbedaan antara Fetch API dan library jQuery dalam AJAX:
   - Fetch API:
     Tidak memerlukan unduhan library tambahan, karena Fetch API adalah bagian dari JavaScript.
     Menggunakan teknologi yang lebih modern dan mendapat pembaruan teratur dari komunitas pengembang.
     Lebih mudah dalam menangani respons asinkron karena menggunakan Promise.

   - jQuery:
     Cocok untuk proyek dengan tingkat kompatibilitas yang tinggi di berbagai browser.
     Menyediakan antarmuka yang lebih kompleks dan spesifik.
     Lebih hemat waktu karena memiliki fitur-fitur yang disederhanakan untuk keperluan UI.
     Dalam memilih antara Fetch API dan jQuery, keputusan sebaiknya didasarkan pada tujuan dan spesifikasi aplikasi web yang akan dibuat. Jika kebutuhan aplikasi lebih modern dan simpel, maka Fetch API bisa menjadi pilihan yang baik. Namun, jika aplikasi memerlukan UI yang canggih dan kompleks, maka penggunaan jQuery bisa lebih sesuai.

5. Selain itu, penerapan checklist untuk proyek melibatkan langkah-langkah seperti:
   - Membuat fungsi "get product json" di "views.py" yang mengimplementasikan filter user.
   - Membuat routing URL untuk "get product" di "urls.py".
   - Menghapus card yang ada di bagian HTML pada "main.html," tetapi mempertahankan elemen div dengan ID "product_card" agar dapat dipanggil melalui AJAX.
   - Membuat script AJAX yang mencakup fungsi "getProduct" yang dinyatakan sebagai asinkron, serta fungsi "refreshProduct."
   - Membuat fungsi "add_product" AJAX di "views.py" dan menentukan routing URL-nya.
   - Membuat modal Bootstrap berupa tabel untuk mengisi formulir "add new product," seperti harga, dan lainnya di HTML.
   - Membuat tombol "add new product."
   - Membuat script AJAX POST untuk tombol "addProduct" saat formulir disubmit dan menambahkan fungsi "onclick" saat tombol "add product" ditekan.
   - Melakukan perintah "collectstatic" di terminal.
   - Melakukan deploy aplikasi web.



Tugas 5

1. Jelaskan manfaat dari setiap jenis selector CSS dan kapan tepat menggunakannya.
Jawab : 
- Element Selector: Untuk mengubah properti elemen dengan tag yang sama, cocok untuk aplikasi gaya umum pada elemen serupa.
- ID Selector: Digunakan untuk elemen dengan ID unik, cocok untuk merubah gaya elemen tertentu.
- Class Selector: Mengubah gaya sekelompok elemen dengan karakteristik yang sama.


2.HTML tag yang saya ketahui :
Jawab :
>  - &lt;p&gt; --> untuk membuat pargraf
>  - &lt;title&gt; --> Untuk judul halaman.
>  - &lt;body&gt; ---> Untuk badan halaman.
>  - &lt;h1&gt; sampai - &lt;h6&gt; --> Untuk judul dengan ukuran berbeda.
>  - &lt;b&gt; --> Untuk teks tebal.
>  - &lt;style&gt; --> Untuk mengatur gaya elemen dengan CSS.


3.Perbedaan antara margin dan padding:
Jawab :
Margin: Mengatur jarak antara elemen dengan elemen lainnya di luar border, hanya mengatur jarak.
Padding: Mengatur jarak antara konten elemen dan tepi elemennya, juga mengatur latar belakang dan warna elemen.
Perbedaan antara Tailwind CSS dan Bootstrap:

4. Perbedaan antara framework CSS Tailwind dan Bootstrap
Jawab :
Tailwind CSS: Menggabungkan kelas utilitas yang sudah didefinisikan, lebih fleksibel, lebih sulit untuk dipelajari.
Bootstrap: Menggunakan komponen yang sudah didefinisikan, lebih konsisten, lebih mudah dipelajari.


5. Penjelasan step by step :
Jawab :
Menambahkan Bootstrap ke aplikasi.
Merancang halaman login dengan card dan mengubah latar belakang.
Merancang halaman create product dengan mengubah latar belakang dan margin.
Merancang halaman register dengan card, margin, dan latar belakang.
Merancang halaman main dengan navigasi bar Bootstrap, card untuk produk, tombol edit, dan mengubah latar belakang.
Menambahkan tombol edit product dan membuat halaman edit_product.
Membuat readme dan melakukan git add, commit dan push ke GitHub.





Tugas 4
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
> Jawab :
> UserCreationForm pada Django merupakan function yang berfungsi untuk membuat akun user baru pada web application development Django. Dengan memanfaatkan function ini, user dapat membuat akun dengan mengisi field username, password1, dan password2 (confirm password).

> Kelebihan Django UserCreationForm : menerima karakter ASCII dan Unicode, bisa diasosiasikan dengan email (namun tidak wajib), mudah digunakan,  menyediakan fitur validasi otomatis seperti format username yang tepat, password yang sesuai dengan kebijakan keamanan, serta password konfirmasi yang harus sama dengan password sebelumnya.

> Kekurangan Django UserCreationForm : username tidak case-insensitive, serta akun tanpa password tidak bisa di reset passwordnya.

2.Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
> Jawab :

> Autentikasi : Proses yang memverifikasi akun user, apakah sudah sesuai username dan password yang diinput dengan yang ada pada database.

> Otorisasi: Proses yang menentukan apa saja yang user terautentikasi boleh lakukan.

> Why important?: Menjaga kemanan web aplikasi yang dibuat agar tidak sembarang orang bisa masuk. Selain itu, adanya otorisasi membuat data yang dimiliki terjaga privasinya karena hanya user yang diautentikasi saja yang dapat mengakses datanya masing-masing.

3.Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
> Jawab :
> Cookies merupakan sepotong data berbentuk teks yang berisikan data dan informasi user yang disimpan dalam browser. Cookies berfungsi untuk meningkatkan personalisasi akun user dengan menyimpan data relevan user dan menampilkannya lagi ketika user mengakses browser yang sama. Dalam Django, kita bisa menambah cookies dengan mengimplementasikan function set_cookie('cookie_name', 'cookie-value') dan get('cookie_name'), kita juga bisa memberi waktu berakhirnya cookies tersebut dengan function set_cookie(key, value='', max_age=None, expires=None) selama None diubah dengan waktu yang diinginkan.

4.Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
> Jawab :
> Umumnya, cookies dapat dikatakan aman dalam pengembangan web, namun terkadang masih ada risiko keamanan jika menggunakan cookies. Contohnya, jika ada informasi yang sensitif dalam akun user, maka seorang hacker dapat mencuri data tersebut dan menyalahgunakannya untuk hal lain. Contoh lain dapat terjadi sebaliknya, di mana seorang hacker dapat menyusupkan virus dan malware ke komputer kita dengan cara menyamarkannya dalam bentuk cookies. Namun, hal-hal tersebut harusnya tidak terjadi selama keamanan website masih tinggi dan tidak ada celah-celah yang bisa dieksploitasi.

5.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> Jawab :
>
> Langkah pertama adalah saya membuat 3 fungsi baru, yaitu:

  > - register untuk membuat akun user. Dengan menggunakan UserCreationForm Django untuk menangani pembuatan akun baru bagi user.

  > - login_user untuk proses login. Dengan menggunakan function authenticate dan login yang diimport dari Django untuk menghandle autentikasi dan login saat autentikasi berhasil.

  > - logout_user untuk logout dari halaman utama.

> Langkah kedua adalah saya membuat berkas baru yaitu register.html dan login.html untuk tampilan login dan registernya. Tak lupa juga untuk menambahkan tampilan tombol logout di berkas main.html.

> Ketiga saya melakukan routing untuk tampilan login, logout, dan register.

> Keempat, merestriksi akses halaman Main agar login terlebih dahulu dengan menambahkan kode @login_required(login_url='/login') di atas fungsi show_main.

> Kelima, setelah menjalankan runserver, saya membuat dua akun baru di section register.
  Berikut akunnya:
  username1: sita.amira; pass: Erza12345
  username2: erza.scarlet; pass: PBP12345


> Keenam, menghubungkan model Product dengan User dengan cara:
  > - Mengimport modul User dari django.contrib.auth.models, lalu menambahkan model user ke class Product dengan menggunakan code user = models.ForeignKey(User, on_delete=models.CASCADE)

  > - Mengedit fungsi create_product agar Django tidak langsung menyimpan objek yg di buat ke database.

  > - Mengubah fungsi show_main pada bagian 'name' agar yang muncul merupakan username yang sedang login.

  > - Melakukan makemigration dan migrate.

  > - Mengimpor date time. Lalu di login_user membuat fungsi baru yang dapat menambahkan cookie.

  > - Menambahkan last_login pada show_main

  > - Mengubah logout_user untuk menghapus cookie setiap kali logout

  > - Menambahkan teks last login pada main.html agar muncul di tampilan layar.

> Terakhir, untuk pengerjaan soal bonus:
  > - Membuat fungsi add_product dan sub_product pada views.py (subdirektori main) yang kodenya kurang lebih sama. Dengan mencari product berdasarkan id yang tombolnya dipencet. Kemudian menambahkan logika pengurangan atau pengurangan didalamnya.

  > - Melakukan routing pada urls.py untuk fungsi add_product dan sub_product

  > - Membuat tampilan buttonnya di main.html

  > - Membuat fungsi delete_product di views.py yang kodenya kurang lebih sama dengan add_product dan sub_product. Hanya saja product.save() tidak ada pada fungsi delete product.

  > - Melakukan routing pada urls.py untuk fungsi delete_product serta membuat tampilan buttonnya di main.html.

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

5. Screenshot dari hasil akses URL pada Postman
![Screenshot (48)](https://github.com/sitaamirasyarifah/SMart/assets/122429830/de53985f-b0a7-4c0b-840c-9a4138b38e98)
![Screenshot (52)](https://github.com/sitaamirasyarifah/SMart/assets/122429830/a42ffc33-6ce3-47ed-abfe-9add1f77bcd2)
![Screenshot (51)](https://github.com/sitaamirasyarifah/SMart/assets/122429830/5a0322c2-452d-4f33-8384-de5d6a555340)
![Screenshot (50)](https://github.com/sitaamirasyarifah/SMart/assets/122429830/8608cbef-b5b6-470d-9133-ca01131dd4d0)
![Screenshot (49)](https://github.com/sitaamirasyarifah/SMart/assets/122429830/66616701-cffc-4869-b3f9-75b8d44dcd80)

















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
=======
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

