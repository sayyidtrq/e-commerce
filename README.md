Nama : Sayyid Thariq Gilang Muttaqien
NPM  : 2306275714
Kelas : B

link web tugas 2:
http://sayyid-thariq31-temuhobi.pbp.cs.ui.ac.id/



Pertanyaan: 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

5. Mengapa model pada Django disebut sebagai ORM?

Jawaban:

1.  - Membuat Proyek Django Baru
    step by step
    1. Membuat repositori baru dan juga folder lokal lalu hubungkan keduanya dengan cara inisialisasi git dalam folder lokal dan push kepada repositori github
    2. Konfigurasi env dengan menuliskan syntax "python -m venv env" pada terminal folder lokal
    3. Mengaktifkan scripts env dengan syntax "env/Scripts/activate"
    4. Menginstal django melalui terminal dengan command "pip install django"
    5. Lalu setelah proses pengistallan selesai tuliskan command "django-admin startproject <nama project>" pada terminal folder lokal
    6. Django telah terinstall

    - Membuat aplikasi bernama main
    1. Melakukan command di terminal "django-admin startapp main"
    2. Lalu folder main akan terbuat sebagai branch dari folder utama

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    1. Pada settings.py di folder project kita cari variabel INSTALLED_APPS
    2. Tambahkan main pada installed apps tersebut
    3. Atur dan ubah urls.py pada folder project sesuai dengan keinginan kita adn masukan main pada kodenya

    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    1. Pada models.py di apps main ubah buat attribute dan datatypenya serta limitasi penulisan datatypenya 
    2. Setelah sudah merubah/membuat lakukan "python manage.py makemigration" untuk memberikan migrasi pada model data yang belum diapply ke model
    3. lalu lakukan "python manage.py migrate" untuk apply perubahan tersebut apda data

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    1. Menuliskan attribute yang tadi sudah dibuat dan coba masukan nilai ke dalamnya untuk dishow pada html
    2. Perhatikan data type, jangan sampai salah
    3. return dengan format seperti ini return render(request, "main.html", context)
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    1. tulis code berikut app_name = 'main'
        urlpatterns = [
            path('', show_main, name='show_main'),
        ]

        pada urls.py dalam main
        ini berfungsi apabila path/ url sama dengan kosong maka ia akan show_main ambil fungsi show_main dari views yang mengembalikan html 

    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    1. buat project baru di pwsnya
    2. melakukan git remote add <url>
    3. git branch -M main
    4. git push pws main:master
    5. tunggu build lalu selesai

    Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    - ini gausah , karena sangat mudah
    

2. berikut bagan dan penjelesannya https://docs.google.com/document/d/1uYkG4FoWOHOEJsm158XuZvZx0qlP1KN8iJeCz1XC9RA/edit?usp=sharing 

3.  Git adalah sistem kontrol versi untuk melacak perubahan dalam berkas komputer dan mengoordinasikan pekerjaan pada berkas tersebut di antara banyak orang. Fungsi Git yang paling mendasar dan penting adalah memungkinkan tim untuk menambahkan (dan menggabungkan) kode pada saat yang sama ke proyek yang sama. Dengan menambahkan kemampuan ini ke proyek, tim menjadi lebih efisien dan memberi mereka kemampuan untuk mengerjakan proyek yang lebih besar dan masalah yang lebih kompleks. Ada juga banyak hal lain yang dilakukan Git dengan sangat baik: ia memungkinkan kita mengembalikan perubahan, membuat cabang baru untuk menambahkan fitur baru, menyelesaikan konflik penggabungan, dan seterusnya.

4.  
    1. Bahasa pemrograman python, seperti yang kita tahu python adalah salah astu high level language sehingga mempermudah    user membuat back-end programnya , python merupakan salah satu bahasa pemrograman yang memiliki syntax yang mudah
    2. Banyak fitur bawaaan, engguna tidak perlu mencari atau mengonfigurasi banyak library eksternal untuk menjalankan fitur umum seperti otentikasi, manajemen pengguna, sistem admin, formulir, atau keamanan (CSRF, XSS, dll.). Hal ini membuat Django ideal bagi pemula yang belum memiliki pengalaman banyak dalam pengelolaan dependensi.
    3. Django memiliki komunitas yang besar dan aktif, sehingga mudah untuk menemukan bantuan, tutorial, atau solusi untuk masalah yang dihadapi pemula. Banyak sumber daya pembelajaran seperti forum, kursus online, blog, dan video tutorial yang tersedia.
    4. Django memiliki fokus yang kuat pada keamanan. Misalnya, Django secara otomatis melindungi aplikasi dari serangan umum seperti Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), SQL Injection, dan lainnya. Fitur keamanan bawaan ini memungkinkan pemula untuk fokus pada pengembangan fitur tanpa khawatir terhadap aspek keamanan yang kompleks.

5.  Karena pada django menyediakan fitur yang memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek Python, alih-alih menulis kode SQL secara langsung. Dengan Django ORM, pengembang dapat melakukan operasi database seperti query, insert, update, dan delete menggunakan metode Python tanpa perlu memahami atau menulis SQL. 
      
