# NAMA : Ketrin Vani Andini
# NIM  : 20210801348
# TUGAS SESI 6 PBO

class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def getJam(self):
        return self.hour

   
    def getMenit(self):
        return self.minute
    

    def getDetik(self):
        return self.second

waktu = Time(10,10,12)

if waktu.hour <= 24 and waktu.minute <= 59 and waktu.second <= 59:
    print("Waktu saat ini adalah : jam {}, lewat {} menit, {} detik".format(waktu.getJam() ,  waktu.getMenit() , waktu.getDetik()))

else:
    print("ERROR! Format waktu yang di input salah! ")




