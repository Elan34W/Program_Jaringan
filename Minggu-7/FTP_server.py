import ftplib

def upload_file(hostname, username, password, filename):
    try:
        # Membuat objek FTP
        ftp = ftplib.FTP(hostname)

        # Login ke server FTP
        ftp.login(username, password)

        # Buka file untuk dibaca
        with open(filename, 'rb') as file:
            # Unggah file mp4
            ftp.storbinary('STOR ' + filename, file)

        # Tutup koneksi FTP
        ftp.quit()

        print("File berhasil diunggah.")

    except ftplib.all_errors as e:
        print("Terjadi kesalahan: ", e)

# Contoh penggunaan fungsi upload_file
hostname = 'localhost'
username = 'elanagumw'
password = 'd4c3b2a1'
filename = 'chad_shaggy.mp4'

upload_file(hostname, username, password, filename)