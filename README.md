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

# TUGAS 5 #

##  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! ##
- Urutan prioritas pengambilan CSS selector adalah sebagai berikut:
    1. Inline CSS: Inline CSS memiliki prioritas tertinggi karena didefinisikan langsung pada elemen HTML.
    2. Internal CSS: Internal CSS memiliki prioritas kedua setelah Inline CSS karena didefinisikan pada tag <style> di dalam tag <head>.
    3. External CSS: External CSS memiliki prioritas terendah karena didefinisikan pada file eksternal CSS yang dihubungkan dengan tag <link> di dalam tag <head>.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design! ##

- Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena memungkinkan tampilan aplikasi web menyesuaikan ukuran layar perangkat pengguna. Dengan responsive design, pengguna dapat mengakses aplikasi web dengan nyaman dan mudah tanpa harus memperbesar atau memperkecil tampilan. Hal ini meningkatkan pengalaman pengguna dan memastikan aplikasi web dapat diakses oleh berbagai perangkat, seperti desktop, tablet, dan smartphone. Contoh aplikasi yang sudah menerapkan responsive design adalah Google, Facebook, dan Twitter. Sedangkan contoh aplikasi yang belum menerapkan responsive design adalah aplikasi web yang tampilannya tidak menyesuaikan ukuran layar perangkat pengguna sehingga terlihat terpotong atau tidak rapi.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! ##

- Margin adalah jarak antara elemen HTML dengan elemen lain di sekitarnya. Margin digunakan untuk memberikan ruang kosong di sekitar elemen. Border adalah garis yang mengelilingi elemen HTML. Border digunakan untuk membatasi elemen dan memberikan efek visual. Padding adalah jarak antara konten elemen HTML dengan border. Padding digunakan untuk memberikan ruang kosong di antara konten dan border. Untuk mengimplementasikan margin, border, dan padding, kita dapat menggunakan properti CSS berikut:
    - Margin: margin-top, margin-right, margin-bottom, margin-left
    - Border: border-top, border-right, border-bottom, border-left
    - Padding: padding-top, padding-right, padding-bottom, padding-left

## Jelaskan konsep flex box dan grid layout beserta kegunaannya! ##

- Flexbox adalah model layout CSS yang dirancang untuk menyusun elemen HTML dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox memungkinkan pengembang web untuk membuat tata letak yang responsif dan fleksibel tanpa menggunakan float atau positioning. Flexbox memiliki properti seperti justify-content, align-items, dan flex-direction yang memudahkan pengembang web untuk mengatur tata letak elemen. Grid layout adalah model layout CSS yang dirancang untuk menyusun elemen HTML dalam dua dimensi, baik secara baris maupun kolom. Grid layout memungkinkan pengembang web untuk membuat tata letak yang kompleks dan terstruktur dengan mudah. Grid layout memiliki properti seperti grid-template-columns, grid-template-rows, dan grid-gap yang memudahkan pengembang web untuk mengatur tata letak

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! ##

### Kustomisasi halaman login, register, dan tambah product semenarik mungkin. ###
- implementasi styling menggunakan tailwind css , dengan tipe inline css dan internal css
- menambahkan background image, warna, font, dan ukuran yang sesuai
- menambahkan animasi dan transisi untuk membuat tampilan lebih menarik
- menyesuaikan layout dan posisi elemen agar terlihat rapi dan mudah dibaca

### Kustomisasi halaman daftar product menjadi lebih menarik dan responsive ###
```html
    <section id="goodies" class="py-12 mb-20 mt-15">
      <h2 class="text-3xl font-extrabold text-center mb-8">PRODUCT EXAMPLE</h2>
      <div class="flex space-x-4 overflow-x-scroll px-10 scrollbar-hide" style="scrollbar-width: none; -ms-overflow-style: none; margin-right:15px;">
        <img src="{% static 'images/ronaldo (1).png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-50 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/barca.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/jordan1.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/jordan2.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/jordan3.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/char.png' %}" alt="{{name}}" class="w-60 h-60% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/hw1.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
        <img src="{% static 'images/hw2.png' %}" alt="{{name}}" class="w-60 h-75% object-contain transition-transform duration-30 ease-in-out transform hover:scale-110 hover:shadow-lg"style="padding:15px">
      </div>
    </section>
    <section id="add-item" class="py-12">
    <div class="flex flex-col md:flex-row justify-center space-y-4 md:space-x-4 md:space-y-0 items-center">
          <a href="{% url 'main:create_item' %}">
              <button class="bg-black text-white py-2 px-6 rounded-lg hover:bg-gray-800 transition transform hover:scale-105">Add New Item</button>
          </a>
      </div>
      {% if not itemEntry %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
          <img src="{% static 'images/sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
          <p class="text-center text-gray-600 mt-4">Belum ada data item pada web</p>
      </div>
      {% else %}
      <div class="flex space-x-4 overflow-x-scroll px-10 scrollbar-hide mt-[20px]" style="scrollbar-width: none; -ms-overflow-style: none; margin-right:15px;">
          {% for item_entry in itemEntry %}
              {% include 'card_item.html' with item_entry=item_entry %}
          {% endfor %}
      </div>
      {% endif %}
      <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8 mt-[30px] mx-[20px]">
        {% include "card_info.html" with title='NPM' value=npm %}
        {% include "card_info.html" with title='Name' value=nama_owner %}
        {% include "card_info.html" with title='Class' value=kelas %}
      </div>
      <h5 class="text-center mt-2">Sesi terakhir login: {{ last_login }}</h5>
    </div>
  </section>
```

### Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar  ###

```html
   {% if not itemEntry %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
          <img src="{% static 'images/sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
          <p class="text-center text-gray-600 mt-4">Belum ada data item pada web</p>
      </div>
      {% else %}
```

### Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!). ###

```html
    <div class="flex space-x-4 overflow-x-scroll px-10 scrollbar-hide mt-[20px]" style="scrollbar-width: none; -ms-overflow-style: none; margin-right:15px;">
          {% for item_entry in itemEntry %}
              {% include 'card_item.html' with item_entry=item_entry %}
          {% endfor %}
      </div>
      {% endif %}
      <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8 mt-[30px] mx-[20px]">
        {% include "card_info.html" with title='NPM' value=npm %}
        {% include "card_info.html" with title='Name' value=nama_owner %}
        {% include "card_info.html" with title='Class' value=kelas %}
      </div>
      <h5 class="text-center mt-2">Sesi terakhir login: {{ last_login }}</h5>
    </div>
```

###  Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!  ###
```html
    <div class = "rounded-xl shadow-lg bg-gray-400 p-4 hover:animate-pulse">
    <div class = "p-5 flex flex-col"> 
        <div class= "rounded-xl overflow-hidden">
            <h1 class = "text-2xl font-semibold text-center">{{item_entry.name}}</h1>
            <p class = "text-center text-gray-600">{{item_entry.description}}</p>
            <p class = "text-center text-gray-600">Rp{{item_entry.price}}</p>
            <p class = "text-center text-gray-600">{{item_entry.rarity}}/10</p>
            <p class = "text-center text-gray-600">{{item_entry.kategories}}</p>
            <div class = "flex justify-center gap-[15px] mt-[8px]">
                <a href="{% url 'main:edit_item' item_entry.pk %}">
                    <button class = "bg-blue-600 text-white py-2 px-6 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Edit</button>
                </a>
                <a href="{% url 'main:delete_item' item_entry.pk %}" onclick="return confirmDelete()">
                    <button class = "bg-red-600 text-white py-2 px-6 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Delete</button>
                </a>
            </div>
        </div>
    </div>
</div>
```

###  Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop. ###
```html
<!-- Mobile Navigation -->
<div class="md:hidden fixed top-0 left-0 w-full bg-white shadow-lg py-4 px-8 z-50 flex justify-between items-center">
    <div class="text-xl font-semibold">
        <span class="text-gray-600">Temu</span>
        <span class="text-black">Hobi</span>
    </div>
    <div class="block md:hidden">
        <!-- Hamburger button -->
        <button id="hamburger" class="focus:outline-none">
            <svg id="hamburger-icon" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path> </svg>
            <!-- Close (X) button, hidden initially -->
            <svg id="close-icon" class="w-6 h-6 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path> </svg>
        </button>
    </div>
</div>
                
<!-- Mobile Menu -->
<ul id="mobile-menu" class="md:hidden fixed top-16 left-0 w-full bg-white shadow-lg py-4 px-8 z-40 hidden">
    <li class="hover:text-black transition transform hover:scale-110 cursor-pointer"><a href='#home'>Home</a></li>
    <li class="hover:text-black transition transform hover:scale-110 cursor-pointer"><a>About</a></li>
    <li class="hover:text-black transition transform hover:scale-110 cursor-pointer"><a>On Sales</a></li>
    <li class="hover:text-black transition transform hover:scale-110 cursor-pointer"><a>New Arrival</a></li>
    <li class="hover:text-black transition transform hover:scale-110 cursor-pointer"><a href="{% url 'main:logout' %}">
        <button class="bg-red-400 text-white py-1 px-2 rounded-lg hover:bg-red-600 transition transform hover:scale-110" style="font-size: 0.8rem">Logout</button>
    </a></li>
</ul>

<!-- Script to handle menu toggle -->
<script>
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const closeIcon = document.getElementById('close-icon');

    // Toggle the mobile menu and change icons
    hamburger.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        hamburgerIcon.classList.toggle('hidden');
        closeIcon.classList.toggle('hidden');
    });
</script>
```

# Tugas 6 #

### Mengubah tugas 5 menjadi menggunakan AJAX ###

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas). ###

#### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web! ####
- JavaScript memungkinkan pengembang untuk membuat aplikasi web yang interaktif dan dinamis.
- JavaScript memungkinkan pengembang untuk membuat aplikasi web yang responsif terhadap input pengguna.
- JavaScript memungkinkan pengembang untuk membuat aplikasi web yang dapat berkomunikasi dengan server tanpa perlu me-refresh halaman.
- JavaScript memungkinkan pengembang untuk membuat aplikasi web yang dapat berjalan di berbagai platform dan perangkat.

#### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?####
- await digunakan untuk menunggu hingga fetch() selesai mengambil data dari server.
- Jika tidak menggunakan await, fetch() akan mengembalikan Promise yang belum selesai, sehingga kode selanjutnya akan dijalankan sebelum fetch() selesai.
- Dengan menggunakan await, kode selanjutnya akan dijalankan setelah fetch() selesai, sehingga kita dapat memastikan bahwa data yang diambil sudah tersedia sebelum kode selanjutnya dijalankan.

#### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST? ####
- Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST agar request POST yang dikirimkan melalui AJAX tidak memerlukan token CSRF.
- Jika kita tidak menggunakan csrf_exempt, maka Django akan menolak request POST yang dikirimkan melalui AJAX karena tidak menyertakan token CSRF.
- Dengan menggunakan csrf_exempt, kita memastikan bahwa request POST yang dikirimkan melalui AJAX dapat diterima oleh Django tanpa memerlukan token CSRF.

#### pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja? ####
- Pembersihan data input pengguna dilakukan di belakang (backend) juga untuk memastikan bahwa data yang disimpan di basis data sudah bersih dan aman.
- Jika pembersihan data dilakukan di frontend saja, maka data yang disimpan di basis data masih bisa saja mengandung kode berbahaya atau data yang tidak valid.
- Dengan melakukan pembersihan data di belakang (backend), kita dapat memastikan bahwa data yang disimpan di basis data sudah bersih dan aman dari serangan XSS atau SQL Injection.

#### Menjelaskan Checklist diatas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ####

#### AJAX get ####
- ubahlah kode cards data mood agar dapat menggunakan AJAX GET
```javascript
   async function refreshItemEntries(){
    document.getElementById("item_entry_cards").innerHTML = "";
    document.getElementById("item_entry_cards").className = "";
    const itemEntries = await getItemEntries();
    let htmlString = "";
    let classNameString ="";
    if(itemEntries.length === 0){
      classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
      htmlString = `
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'images/sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data item pada web</p>
        </div>
      `;
    }
    else{
      classNameString = "relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8 mt-[30px] mx-[20px]";
      itemEntries.forEach((item) => {
        const name = DOMPurify.sanitize(item.name);
        const price = DOMPurify.sanitize(item.price);
        const description = DOMPurify.sanitize(item.description);
        const rarity = DOMPurify.sanitize(item.rarity);
        const rating = DOMPurify.sanitize(item.rating);
        const image_url = DOMPurify.sanitize(item.image_url);
        htmlString += `
        <div class="rounded-xl my-[15px] shadow-lg bg-white transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-xl w-[300px] h-[400px]">
          <div class="flex flex-col h-full">
              <!-- Image Section -->
              <div class="rounded-t-xl">
                  <img src=${item.fields.image_url} alt=${item.fields.name} class="w-full h-40 object-contain shadow-md">
              </div>

              <!-- Text Section -->
              <div class="text-area p-4 flex-1 flex flex-col justify-between">
                  <!-- Rating and Categories --> 
                  <div class="rating-kategories px-2 flex justify-center mb-2 space-x-2">
                      <p class="py-1 px-2 text-gray-700 text-xs font-semibold rounded-md border bg-neutral-300 inline-block">${item.fields.kategories}</p>
                      <p class="py-1 px-2 text-gray-800 text-xs font-semibold rounded-md border bg-neutral-400 inline-block">${item.fields.rating}/10</p>
                  </div>

                  <!-- Item Name -->
                  <h1 class="text-stone-800 text-lg font-semibold text-left animate-pulse">${item.fields.name}</h1>

                  <!-- Price -->
                  <p class="mt-1 text-stone-600 text-md font-bold text-left">Rp${item.fields.price}</p>

                  <!-- Scrollable Description -->
                  <div class="mt-2 text-gray-600 text-xs h-16 overflow-y-auto overflow-x-hidden" style="scrollbar-width: none; -ms-overflow-style: none;">
                      <p class="text-center">${item.fields.description}</p>
                  </div>

                  <!-- Action Buttons -->
                  <div class="flex justify-center gap-4 mt-4">
                      <a href="/edit-item/${item.pk}">
                          <button class="bg-neutral-400 text-white py-1 px-3 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Edit</button>
                      </a>
                      <a href="/delete/${item.pk}" onclick="return confirmDelete()">
                          <button class="bg-red-900 text-white py-1 px-3 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Delete</button>
                      </a>
                  </div>
              </div>
          </div>
      </div>
        `;
      })
    }
    document.getElementById("item_entry_cards").innerHTML = htmlString;
    document.getElementById("item_entry_cards").className = classNameString;
  }
```
- Lakukan pengambilan data menggunakan AJAX GET

```javascript
    async function getItemEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
    //views.py
    def show_xml(request):
        data = ItemEntry.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = ItemEntry.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```

#### AJAX post ####
- Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
```html
   <div id="crudModal" class="hidden fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
                <h3 class="text-xl font-semibold text-gray-900">Add New Item Entry</h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="px-6 py-4 space-y-6 form-style">
                <form id="itemEntryForm">
                    <div class="mb-2">
                        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                        <input type="text" id="name" name="name" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                        <input type="number" id="price" name="price" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                        <textarea id="description" name="description" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required></textarea>
                    </div>
                    <div class="mb-2">
                        <label for="image_url" class="block text-sm font-medium text-gray-700">Image URL</label>
                        <input type="url" id="image_url" name="image_url" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="rating" class="block text-sm font-medium text-gray-700">Rating</label>
                        <input type="number" id="rating" name="rating" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="kategories" class="block text-sm font-medium text-gray-700">Categories</label>
                        <input type="text" id="kategories" name="kategories" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="rarity" class="block text-sm font-medium text-gray-700">Rarity</label>
                        <input type="text" id="rarity" name="rarity" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                </form>
                <!-- Modal footer -->
                <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                    <button type="submit" id="submitItemEntry" form="itemEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
                </div>
            </div>
        </div>
    </div
```

- Buatlah fungsi untuk menambahkan mood menggunakan AJAX POST
```javascript
    function addItemEntry(){
    fetch("{% url 'main:create_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector("#itemEntryForm")),
    }).then((response) => refreshItemEntries());

    document.getElementById("itemEntryForm").reset();
    document.querySelector("[data-modal-target='crudModal']").click(); // Close the modal after form submission

    return false;
  }

  async function getItemEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
  async function refreshItemEntries(){
    document.getElementById("item_entry_cards").innerHTML = "";
    document.getElementById("item_entry_cards").className = "";
    const itemEntries = await getItemEntries();
    let htmlString = "";
    let classNameString ="";

    if(itemEntries.length === 0){
      classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
      htmlString = `
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'images/sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data item pada web</p>
        </div>
      `;
    }
    else{
      classNameString = "relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8 mt-[30px] mx-[20px]";
      itemEntries.forEach((item) => {
        const name = DOMPurify.sanitize(item.name);
        const price = DOMPurify.sanitize(item.price);
        const description = DOMPurify.sanitize(item.description);
        const rarity = DOMPurify.sanitize(item.rarity);
        const rating = DOMPurify.sanitize(item.rating);
        const image_url = DOMPurify.sanitize(item.image_url);
        htmlString += `
        <div class="rounded-xl my-[15px] shadow-lg bg-white transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-xl w-[300px] h-[400px]">
          <div class="flex flex-col h-full">
              <!-- Image Section -->
              <div class="rounded-t-xl">
                  <img src=${item.fields.image_url} alt=${item.fields.name} class="w-full h-40 object-contain shadow-md">
              </div>

              <!-- Text Section -->
              <div class="text-area p-4 flex-1 flex flex-col justify-between">
                  <!-- Rating and Categories --> 
                  <div class="rating-kategories px-2 flex justify-center mb-2 space-x-2">
                      <p class="py-1 px-2 text-gray-700 text-xs font-semibold rounded-md border bg-neutral-300 inline-block">${item.fields.kategories}</p>
                      <p class="py-1 px-2 text-gray-800 text-xs font-semibold rounded-md border bg-neutral-400 inline-block">${item.fields.rating}/10</p>
                  </div>

                  <!-- Item Name -->
                  <h1 class="text-stone-800 text-lg font-semibold text-left animate-pulse">${item.fields.name}</h1>

                  <!-- Price -->
                  <p class="mt-1 text-stone-600 text-md font-bold text-left">Rp${item.fields.price}</p>

                  <!-- Scrollable Description -->
                  <div class="mt-2 text-gray-600 text-xs h-16 overflow-y-auto overflow-x-hidden" style="scrollbar-width: none; -ms-overflow-style: none;">
                      <p class="text-center">${item.fields.description}</p>
                  </div>

                  <!-- Action Buttons -->
                  <div class="flex justify-center gap-4 mt-4">
                      <a href="/edit-item/${item.pk}">
                          <button class="bg-neutral-400 text-white py-1 px-3 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Edit</button>
                      </a>
                      <a href="/delete/${item.pk}" onclick="return confirmDelete()">
                          <button class="bg-red-900 text-white py-1 px-3 rounded-lg hover:bg-white hover:text-gray-600 transition transform hover:scale-105">Delete</button>
                      </a>
                  </div>
              </div>
          </div>
      </div>
        `;
      })
    }
    document.getElementById("item_entry_cards").innerHTML = htmlString;
    document.getElementById("item_entry_cards").className = classNameString;
  }
```

- Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
```python
    @csrf_exempt
    @require_POST
    def create_item_ajax(request):
        user = request.user
        name = strip_tags(request.POST.get('name'))
        price = strip_tags(request.POST.get('price'))
        description = strip_tags(request.POST.get('description'))
        rarity = strip_tags(request.POST.get('rarity'))
        rating = strip_tags(request.POST.get('rating'))
        kategories = strip_tags(request.POST.get('kategories'))
        image_url = strip_tags(request.POST.get('image_url'))
        new_item = ItemEntry(
            user=user,
            name=name,
            price=price,
            description=description,
            rarity=rarity,
            rating=rating,
            kategories=kategories,
            image_url=image_url
        )
    new_item.save()
    return HttpResponse(b"CREATED ITEM", status=201)
```

- Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
```python
    path('create-ajax/', views.create_item_ajax, name='create_item_ajax'),
```
- Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
```html
    <div id="crudModal" class="hidden fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="flex items-center justify-between p-4 border-b rounded-t">
                <h3 class="text-xl font-semibold text-gray-900">Add New Item Entry</h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="px-6 py-4 space-y-6 form-style">
                <form id="itemEntryForm">
                    <div class="mb-2">
                        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                        <input type="text" id="name" name="name" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                        <input type="number" id="price" name="price" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                        <textarea id="description" name="description" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required></textarea>
                    </div>
                    <div class="mb-2">
                        <label for="image_url" class="block text-sm font-medium text-gray-700">Image URL</label>
                        <input type="url" id="image_url" name="image_url" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="rating" class="block text-sm font-medium text-gray-700">Rating</label>
                        <input type="number" id="rating" name="rating" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="kategories" class="block text-sm font-medium text-gray-700">Categories</label>
                        <input type="text" id="kategories" name="kategories" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                    <div class="mb-2">
                        <label for="rarity" class="block text-sm font-medium text-gray-700">Rarity</label>
                        <input type="text" id="rarity" name="rarity" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" required>
                    </div>
                </form>
                <!-- Modal footer -->
                <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                    <button type="submit" id="submitItemEntry" form="itemEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
                </div>
            </div>
        </div>
    </div>
```

-Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
```html
    <img src=image.png alt="Logo" class="w-32 h-32"/>
```


    













        


