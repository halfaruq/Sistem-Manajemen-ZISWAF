class Donasi:
    def __init__(self, username, password, saldo,pin):
        self.username = username
        self.password = password
        self.__saldo = saldo
        self.__pin = pin
        
    def login(self, username, password):
            if self.username == username and self.password == password:
                print(f"Login Berhasil, selamat datang {self.username} saldo anda saat ini adalah {self.__saldo}\n")
            else:
                raise ValueError("Login gagal, username dan password salah")
            
    def getSaldo(self,pin):
        if self.__pin == pin:
            return self.__saldo
        else:
            raise ValueError("Pin salah")
    
    def setSaldo(self, jumlah,pin):
        if self.__pin == pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                return self.__saldo
            else:
                raise ValueError("Saldo tidak mencukupi")
    def TopUp(self, jumlah, pin):
        if self.__pin == pin:
            self.__saldo += jumlah
            print(f"Top up sebesar {jumlah} berhasil, saldo anda saat ini adalah {self.__saldo}\n")
            return self.__saldo
        else:
            raise ValueError("Pin salah")
            
class Zakat(Donasi):
    def __init__(self, username, password, saldo, pin):
        super().__init__(username, password, saldo, pin)
            
    def hitungZakat(self,jumlahAsset, pin):        
        Nisab = jumlahAsset / 2668000
        if Nisab >= 85:
            jumlahZakat = int(jumlahAsset * 0.025)
            self.setSaldo(jumlahZakat, pin)
            print(f"{self.username} zakat sebesar {jumlahZakat}\n",
                  f"Transaksi berhasil, saldo anda saat ini adalah {self.getSaldo(pin)}\n")
            return jumlahZakat
        else:
            raise ValueError("Anda tidak memiliki kewajiban untuk membayar zakat saat ini")
        
    def MetodePembayaran(self):
        metode = input("Pilih metode pembayaran zakat (transfer/tunai/qris): ")
        if metode == "transfer":
            print("Silakan transfer zakat anda ke rekening berikut: 1234567890 \n")
        elif metode == "tunai":
            print("Silakan datang ke kantor kami untuk membayar zakat secara tunai \n")
        elif metode == "qris":
            print("Silakan scan QRIS berikut untuk membayar zakat: [QRIS.png] \n")
        else:
            raise ValueError("Metode pembayaran tidak valid, silakan pilih antara 'transfer' atau 'tunai'")
        
          
class Infaq(Donasi):
    def __init__(self, username, password, saldo, pin):  
        super().__init__(username, password, saldo, pin)
            
    def infaq(self,jumlahInfaq, pin):
        self.setSaldo(jumlahInfaq, pin)
        print(f"{self.username} infaq anda sebesar {jumlahInfaq}\n",
              f"Transaksi berhasil, saldo anda saat ini adalah {self.getSaldo(pin)}\n")
        return jumlahInfaq
    def MetodePembayaran(self):
        metode = input("Pilih metode pembayaran infaq (transfer/tunai/qris): ")
        if metode == "transfer":
            print("Silakan transfer infaq anda ke rekening berikut: 1234567890 \n")
        elif metode == "tunai":
            print("Silakan datang ke kantor kami untuk membayar infaq secara tunai \n")
        elif metode == "qris":
            print("Silakan scan QRIS berikut untuk membayar infaq: [QRIS.png] \n")
        else:
            raise ValueError("Metode pembayaran tidak valid, silakan pilih antara 'transfer' atau 'tunai'")
        

class Wakaf(Donasi):
    def __init__(self, username, password, saldo, pin):
        super().__init__(username, password, saldo, pin)
        
    def wakaf(self,pin):
        bentukWakaf = input("Masukkan bentuk wakaf yang ingin anda wakafkan (uang/barang): ")
        jangkawaktu = input("Masukkan jangka waktu wakaf yang ingin anda wakafkan: ")
        if bentukWakaf == "uang":
            jumlahWakaf = int(input("Masukkan jumlah uang yang ingin anda wakafkan: "))
            self.setSaldo(jumlahWakaf, pin)
            print(f"{self.username} wakaf uang sebesar {jumlahWakaf} dengan jangka waktu {jangkawaktu}\n",
                  f"Transaksi berhasil, saldo anda saat ini adalah {self.getSaldo(pin)}\n")
            self.MetodePembayaran()
            return jumlahWakaf
          
        elif bentukWakaf == "barang":
            jenisBarang = input("Masukkan jenis barang yang ingin anda wakafkan: ")
            nilaiBarang = input("Masukkan nilai barang yang ingin anda wakafkan: ")
            print(f"{self.username} mewakafkan {jenisBarang}nya dengan nilai {nilaiBarang} dengan jangka waktu {jangkawaktu}\n",)
            return jenisBarang, nilaiBarang
        else:
            raise ValueError("Bentuk wakaf tidak valid, silakan pilih antara 'uang' atau 'barang'")
        
    def MetodePembayaran(self):
        metode = input("Pilih metode pembayaran wakaf (transfer/tunai/qris): ")
        if metode == "transfer":
            print("Silakan transfer wakaf anda ke rekening berikut: 1234567890 \n")
        elif metode == "tunai":
            print("Silakan datang ke kantor kami untuk membayar wakaf secara tunai \n")
        elif metode == "qris":
            print("Silakan scan QRIS berikut untuk membayar wakaf: [QRIS.png] \n")
        else:
            raise ValueError("Metode pembayaran tidak valid, silakan pilih antara 'transfer' atau 'tunai'") 
    
print("-----Contoh Penggunaan Sistem ZISWAF----- \n")      
#-----Contoh Transaksi zakat-----# 
user1 = Zakat("Ahmad", "Bismillah",25000000, 1234)
user1.login("Ahmad", "Bismillah")
user1.TopUp(5000000, 1234)
user1.getSaldo(1234)
user1.hitungZakat(250000000, 1234)
user1.MetodePembayaran()
#-----Contoh Transaksi infaq-----#
user1 = Infaq("Ahmad", "Bismillah", 25000000, 1234)
user1.infaq(500000, 1234)
user1.MetodePembayaran()
#-----Contoh Transaksi wakaf-----#
user2 = Wakaf("Budi", "Alhamdulillah", 9000000, 5678) 
user2.login("Budi", "Alhamdulillah")
user2.getSaldo(5678)
user2.wakaf(5678)

 