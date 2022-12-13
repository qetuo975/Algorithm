import random
import time
import sys

class Mastermind():
    def __init__(self,Seviye):
        self.Seviye = Seviye
        self.Sayılar = ["0","1","2","3","4","5","6","7","8","9"]
        self.OlusturulanSayı = random.randrange(10 ** Seviye) # Basamak Sayısı Seviye + 1
        self.OlusturulanSayı_STR = str(self.OlusturulanSayı)


        self.Solve()
    def Solve(self):
        UpIndex = 0
        print("Sayı : ",self.OlusturulanSayı,"\n")
        for i in range(1,self.Seviye+1):
            print("\nKontrol edilen basamak sayısı : ",i,"\n")


            for ReferansSayı in self.Sayılar:
                if str(ReferansSayı) == self.OlusturulanSayı_STR[UpIndex]:
                    print("\n---------------------------------------------")
                    print(f"{i}. Basamakta Sayı Bulundu. SONUÇ : +1")
                    print(f"SAYI : {ReferansSayı}")
                    print("---------------------------------------------")
                    UpIndex += 1
                    break
                else:
                    print(f"{i}. Basamakta {ReferansSayı} Bulunamadı. SONUÇ : -1")

        print("\n\n Bilgisayarın Sayısı : ",self.OlusturulanSayı)








                #self.CompilerSayı += j[i-1]













Mastermind(Seviye=5)