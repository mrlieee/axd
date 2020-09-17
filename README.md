# AXD AUTOMATIC XPLOIT DEFACE

AXD adalah Automatic Xploit Deface yang dimana anda menyiapkan file script deface anda lalu memasukkan kedalam folder [axd] ini dengan format .html .php .asp.
setelah anda menyiapkan file anda kedalam folder ini, anda juga menyiapkan beberapa website vuln kedalam file target.txt

###Q&A
A: Bagaimana cara memindahkan file script deface saya kedalam folder ini?
Q: Install mc terlebih dahulu dengan menuliskan 'pkg install mc' setelah itu ada ketik 'mc', Tab kiri anda cari file script deface anda dan Tab kanan anda buka folder axd, lalu klik file anda dan klik COPY>Yes. bisa juga dengan mengenuliskan 'mv NamaScriptDeface.html ~/home/axd

A: Bagaimanan cara memasukkan website kedalam file target.txt?
Q: Buka target.txt dengan menuliskan 'nano target.txt' atau 'vim target.txt', apabila belum install nano atau vim silahkan anda install dengan perintah 'pkg install nano vim'

A: Apakah AXD bisa deface beberapa website?
Q: Bisa, bahkan hingga puluhan ribu website

A: Apakah AXD work?
Q: Tergantung dari website vuln yang telah anda masukkan ke dalam file target.txt
 
# Installation

* Termux:
$ pkg install python2
$ pip2 install requests
$ pkg install git
$ git clone https://github.com/djunekz/axd
$ cd axd
$ python axd.py

* Linux:
$ apt-get install python
$ apt-get install pthon-pip
$ pip install requests
$ apt-get install git
$ git clone https://github.com/djunekz/axd
$ cd axd
$ python axd.py

~Penggunaan:
* Masukkan file script deface anda kedalam folder axd, paste url website kedalam file target.txt (hanya url index (http://www.target.com, https://target.com)

# Install Otomatis:
pkg install python2 && pip2 install requests && pkg install git && git clone https://github.com/djunekz/axd && cd axd && python2 axd.py
