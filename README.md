# GSLC SNA Group 7 -- Docker React Boilerplate



## Menjalankan Project dengan Docker

Untuk menjalankan aplikasi menggunakan Docker jalankan perintah berikut:

``` bash
docker compose up --build
```

Penjelasan:

-   `docker compose up` digunakan untuk menjalankan container
-   `--build` digunakan untuk membangun ulang Docker image jika ada
    perubahan pada konfigurasi



## Menjalankan Container di Background

Jika ingin menjalankan container tanpa membuka terminal terus menerus,
gunakan:

``` bash
docker compose up -d
```



## Mengakses Aplikasi

Setelah container berhasil dijalankan, buka browser dan akses:

http://localhost:3000

Aplikasi React akan berjalan dan dapat diakses melalui alamat tersebut.



## Menghentikan Container

Untuk menghentikan container yang sedang berjalan gunakan perintah:

``` bash
docker compose down
```



## Melihat Container yang Sedang Berjalan

Gunakan perintah berikut untuk melihat container Docker yang aktif:

``` bash
docker ps
```




## Author
Alexander Bagus Wijanarko - 2802407824

Kyoshiro Kaynelie - 2802407553

Mikhael Filemon - 2802471221

