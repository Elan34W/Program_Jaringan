# Tugas 2 - FTP Socket Programming On python

### Nama  : Elan Agum Wicaksono 
### NIM   : 1203220005

## PENDAHULUAN
Program ini mendemonstrasikan File Transfer Protocol (FTP) sederhana menggunakan pemrograman socket dengan Python. Dokumen ini terdiri dari server dan aplikasi klien yang berkomunikasi satu sama lain melalui jaringan.

## SOAL
buat sebuah program file transfer protocol menggunakan socket programming dengan beberapa perintah dari client seperti berikut
1.  ls : ketika client menginputkan command tersebut, maka server akan memberikan daftar file dan folder 
2.  rm {nama file} : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama3.
3.  download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama
4.  upload {nama file} : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama
5.  size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama
6.  byebye : ketika client menginputkan command tersebut, maka hubungan socket client akan diputus
7.  connme : ketika client menginputkan command tersebut, maka hubungan socket client akan terhubung. 

## PENJELASAN

*Server*
*Fungsi-fungsi :*
-  list_files(): Fungsi ini digunakan untuk mendapatkan daftar file dan folder yang ada di direktori server. Menggunakan os.listdir('.') untuk mendapatkan list dari file dan folder di direktori saat ini.
-  remove_file(file_name): Fungsi ini digunakan untuk menghapus file dengan nama tertentu dari server. Jika file ada, maka fungsi ini akan menghapus file tersebut menggunakan os.remove(file_name).
-  download_file(file_name, client_socket): Fungsi ini digunakan untuk mengirim file dengan nama tertentu dari server ke client. Fungsi ini membuka file, membaca datanya, mengirim panjang data terlebih dahulu, lalu mengirim data tersebut ke client.
-  upload_file(file_name, data): Fungsi ini digunakan untuk menerima dan menyimpan file yang diunggah dari client ke server. Jika file dengan nama tersebut sudah ada, maka fungsi ini akan memberikan pesan bahwa file sudah ada. Jika tidak, maka fungsi ini akan menyimpan data yang diterima dari client ke dalam file.
-  file_size(file_name): Fungsi ini digunakan untuk mendapatkan ukuran file dengan nama tertentu di server dalam satuan megabyte (MB).
-  handle_command(command, client_socket): Fungsi ini merupakan pengendali utama yang memproses perintah yang diterima dari client. Fungsi ini akan memanggil fungsi-fungsi yang sesuai berdasarkan perintah yang diterima.

*Client*
*List command yang bisa dipanggil :*
-  connme               : Digunakan untuk menghubungkan client dengan server menggunakan socket.
-  ls                   : Digunakan untuk mendapatkan daftar file dan folder di direktori server, dan kemudian menampilkan hasilnya di terminal.
-  rm(file_name)        : Digunakan untuk menghapus file dengan nama tertentu dari server.
-  download(file_name)  : Digunakan untuk mengunduh file dengan nama tertentu dari server ke direktori lokal client.
-  upload(file_name)    : Digunakan untuk mengunggah file dengan nama tertentu dari direktori lokal client ke server.
-  file_size(file_name) : Digunakan untuk mendapatkan ukuran file dengan nama tertentu di server dalam satuan megabyte (MB), dan kemudian menampilkan hasilnya di terminal.
-  byebye               : Digunakan untuk memutus koneksi antara client dan server, dan kemudian menutup socket client.

