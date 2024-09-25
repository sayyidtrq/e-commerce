# Nama : Sayyid Thariq Gilang Muttaqien #
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
      

TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawab:

Data delivery sudah menjadi pondasi vital dalam pengimplementasian sebuah plaform. Data delivery berfungsi sebagai jembatan ataupun infrastruktur yang memungkinkan berbagai elemen platform untuk berkomunikasi secara seamless. Data pada berbagai elemen, seperti dari server ke klien ataupun sebaliknya, dari database ke user interface dapat mengalir dengan lancar, aman, dan tepat waktu. Tanpa adanya data delivery, maka setiap elemen pada platform akan terisolasi. Hal itu menyebabkan fungsionalitas dari suatu platform akan menjadi tidak sesuai harapan. Selain itu, data delivery yang baik dapat meningkatkan skalabilitas dan memungkinkan platform untuk beradaptasi dengan cepat dengan perubahan kebutuhan dan menangani lonjakan lalu lintas data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jawab:

Dalam format pertukaran data yang umum digunakan, saya memilih JSON untuk digunakan. Banyak aspek yang memengaruhi JSON lebih populer dari XML, seperti:

Kesederhanaan JSON memiliki sintaks yang lebih sederhana. Tidak seperti XML, JSON tidak memerlukan suatu tag pembuka ataupun penutup. Dari segi struktur, JSON memiliki struktur yang mirip dengan object dan array dalam JavaScript
Ukuran File JSON umumnya menghasilkan file dengan ukuran lebih kecil dbandingkan XML karena tidak memerlukan tag penutup
Parsing yang lebih cepat JSON dapat di parse menjadi objek JavaScript dengan sangat cepat
Struktur data yang lebih fleksibel JSON mendukung tipe data, seperti array dan object nested dengan lebih alami
Popularisasi dalam API Banyak API yang menggunakan JSON karena kemudahan dalam penggunaanya
Walaupun XML menawarkan beberapa fitur tambahan seperti mendukung namespace dan skema yang lebih kuat untuk validasi, JSON lebih populer karena lebih ringkas dan mudah dalam pengimplementasiannya.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawab:

Method is_valid() berperan penting dalam proses validasi data yang diinput oleh pengguna. Method ini berfungsi untuk memeriksa apakah data yang disubmit melalui form sudah memenuhi semua aturan validasi, seperti apakah semua field yang required sudah diisi, apakah format data sudah sesuai, atau apakah data sudah memenuhi batasan khusus yang telah didefinisikan. Jika semua data valid, maka is_valid() akan mengembalikan True dan jika ada yang tidak valid, akan mengembalikan False. Selain itu, jika validasi gagal, Django sendiri akan mengisi dictionary form.errors dengan pesan error untuk setiap field yang tidak valid. Selain itu, method ini juga membantu mencegah data yang tidak valid atau berbahaya masuk ke dalam sistem untuk melindungi aplikasi dari potensi bug atau serangan keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawab:

Cross-Site Request Forgery Token merupakan suatu token untuk melindungi aplikasi dari serangan Cross Site Request Forgery. Dengan adanya csrf_token, dapat memastikan bahwa request POST berasal dari situs yang sah dan mencegah modifikasi data yang tidak sah melalui request palsu. Tanpa adanya csrf_token, penyerang akan membuat suatu request palsu menggunakan nama pengguna yang sudah terotentikasi, mengubah data-data sensitif, ataupun informasi pribadi pengguna bisa terekspos dan termanipulasi.

Jika suatu website tidak memiliki csrf_token, maka penyerang akan membuat situs web berbahaya atau memodifikasi situ yang sudah ada. Lalu, pengguna yang sudah login ke aplikasi Django akan tanpa sadar mengakses situs berbahaya tersebut. Setelah itu, situs berbahaya akan memuat form tersembunyi yang mengirim request ke aplikasi Django. Setelah itu, penyerang akan memanfaatkan cookies sesi yang valid dari pengguna. Request palsu akan terlihat sah karena berasal dari browser pengguna yang sudah terotentikasi. Tanpa adanya csrf_token, server tidak dapat membedakan request yang sah dan yang palsu.

Django menghasilkan token unik untuk setiap sesi pengguna. Token ini disertakan dalam setiap form sebagai field tersembunyi. Saat form disubmit, Django akan memeriksa kecocokan token. Jika token berbeda, maka request akan ditolak. Dengan itu, keamanan website akan terjaga.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Membuat base.html untuk menjadi page utama dalam website
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>

        base.html saya kosong kareena saya taro navbar dan homepage layout saya di main

    2. Menambahkan BASE_DIR pada settings.py agar project mengenali html yang akan menjadi template utama
    'DIRS': [BASE_DIR / 'templates'],

    3. Menambahkan atribut time dan id pada model product
    from django.db import models
    import uuid

    class ItemEntry (models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        rarity = models.IntegerField()
        rating = models.IntegerField()
        kategories = models.CharField(max_length=255, default='Sneakers')  
        time = models.DateTimeField(auto_now_add=True) 

    4. Membuat forms.py untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
        
        from django.forms import ModelForm
        from main.models import ItemEntry

        class ItemEntryForm(ModelForm):
            class Meta:
                model = ItemEntry
                fields = ['name', 'price', 'description', 'rarity', 'rating', 'kategories']
                labels = {
                    'name': 'Name',
                    'price': 'Price',
                    'description': 'Description',
                    'rarity': 'Rarity',
                    'rating': 'Rating',
                    'kategories': 'Kategories'
                }
        
    5. Membuat method create_item_entry untuk mengambil input user sesuai dengan forms.py

        def create_item_entry(request):
            if request.method == 'POST':
                form = ItemEntryForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('main:show_main')
            else:
                form = ItemEntryForm()
            return render(request, 'main/create_item_entry.html', {'form': form})
    
    6. Membuat method show_main untuk menampilkannya di main.html
        def show_main(request):
            itemEntry = ItemEntry.objects.all()

            context = {
                'nama_orang': 'Sayyid Thariq',
                'npm': '2306275714',
                'kelas': 'Kelas B',
                'name': 'Jordan 1 Retro High OG',
                'price': 'IDR 2.000.000',
                'description': 'The Air Jordan 1 Retro High OG is a shoe that needs no introduction. It is the shoe that started it all. It is the first ever Air Jordan sneaker released back in 1985, created by the one and only Michael Jordan. The shoe was designed by Peter Moore and it was the only Air Jordan to feature the iconic Nike Swoosh logo. The Air Jordan 1 is still popular today, and has been released in more colorways than any other Air Jordan model.',
                'rarity': '7',
                'rating': '9',
                'kategories': 'Sneakers',
                'itemEntry': itemEntry,
        }

            return render(request, 'main.html', context)

6. SS POSTMAN

https://docs.google.com/document/d/13hFtp96QTZrZNLLXacsUZ_GF2Yfk1NmXjdpMHrSF9CI/edit?usp=sharing 

# TUGAS 4 #

## Apa perbedaan antara HttpResponseRedirect() dan redirect() ##
- HttpResponseRedirect() merupakan class yang berasal dari modul django.http yang digunakan untuk melakukan redirect ke URL yang diberikan. Sedangkan redirect() merupakan shortcut function yang berasal dari modul django.shortcuts yang digunakan untuk melakukan redirect ke URL yang diberikan. 

## Jelaskan cara kerja penghubungan model Product dengan User! ##
- Penghubungan model Product dengan User dilakukan dengan membuat foreign key pada model Product yang merujuk ke model User. Dengan cara ini, setiap data pada model Product akan terhubung dengan data pada model User. Sehingga, setiap data pada model Product akan memiliki informasi tambahan yang terkait dengan data pada model User.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut. ##
- Authentication adalah proses untuk memverifikasi identitas pengguna, yaitu memastikan bahwa pengguna yang login adalah pengguna yang sebenarnya. Sedangkan authorization adalah proses untuk memverifikasi hak akses pengguna, yaitu memastikan bahwa pengguna yang login memiliki hak akses yang sesuai dengan perannya. Saat pengguna login, Django akan melakukan proses authentication untuk memverifikasi identitas pengguna. Setelah pengguna terautentikasi, Django akan melakukan proses authorization untuk memverifikasi hak akses pengguna. Django mengimplementasikan kedua konsep tersebut dengan menggunakan sistem autentikasi dan otorisasi yang terintegrasi. Django menyediakan class User yang digunakan untuk menyimpan data pengguna, seperti username, password, email, dan lainnya. Django juga menyediakan decorator @login_required yang digunakan untuk membatasi akses ke view yang hanya dapat diakses oleh pengguna yang sudah login.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan? ##
- Django mengingat pengguna yang telah login dengan menggunakan session. Saat pengguna login, Django akan membuat session yang berisi informasi pengguna, seperti id pengguna, username, dan lainnya. Session ini akan disimpan di server dan dikirimkan ke pengguna dalam bentuk cookie. Pengguna akan menyimpan cookie ini di browser mereka dan mengirimkannya kembali ke server setiap kali mereka melakukan request. Django akan memeriksa cookie ini untuk mengidentifikasi pengguna yang telah login. Kegunaan lain dari cookies adalah untuk menyimpan informasi pengaturan pengguna, seperti bahasa, tema, dan lainnya. Tidak semua cookies aman digunakan. Cookies yang tidak dienkripsi atau tidak diotentikasi dapat disalahgunakan oleh penyerang untuk mencuri informasi sensitif pengguna atau melakukan serangan lainnya.

## Cara menyelesaikan checklist berikut ##

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. ###

1. Membuat function register_user pada views.py
    ```python
    #registrasi form

    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   
    ```
2. Membuat function login_user pada views.py
    ```python
    #login form

    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```

3. Membuat function logout_user pada views.py
    ```python
    #logout

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

###  Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. ###

1. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    '''python
    #akun yang dibuat
    name : Sayyid.thariq31
    password : Lucario02

    name: Sayyid
    password: Lucario02
    '''

### Menghubungkan model Product dengan User. ###

1. Menghubungkan model Product dengan User
    ```python
    from django.contrib.auth.models import User

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        rarity = models.IntegerField()
        rating = models.IntegerField()
        kategories = models.CharField(max_length=255, default='Sneakers')
        time = models.DateTimeField(auto_now_add=True)
    ```
    ```python
    python manage.py makemigrations
    ```
    ```python
    python manage.py migrate
    ```
### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.###

1. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
    ```python
    def show_main(request):
         itemEntry = ItemEntry.objects.filter(user=request.user)

        context =   {
        'nama_orang': request.user.username,
        'name': '2009 Barcelona Jersey',
        'price': 'Rp. 1.000.000',
        'description': 'Jersey Barcelona tahun 2009 yang dipakai saat final UCL 2009',
        'rarity': 'Legendary',
        'rating': '10',
        'kategories': 'Jersey',
        'nama_owner': 'Sayyid',
        'npm': '2306275714',
        'kelas': 'Kelas B',
        'itemEntry': itemEntry,
        'last_login': request.COOKIES['last_login'],
        }

    return render(request, "main.html", context)
    ```






        


