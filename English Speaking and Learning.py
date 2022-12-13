
import random
import threading
import time
import sqlite3
import speech_recognition as sr
import sys
import os
from pygame import mixer
from gtts import gTTS
from time import sleep


class English():
    def __init__(self, Sleep, Score):
        self.Sleep = Sleep
        self.CON = sqlite3.connect("English.db")
        self.CURSOR = self.CON.cursor()

        self.History = sqlite3.connect("EnglishLocal.db")
        self.HistoryCursor = self.History.cursor()

        self.Türkçe = ""
        self.İngilizce = ""
        self.Microphone_TEXT = ""
        self.EnginnerRandom = 0
        self.EnginnerStop = Score
        self.EnginnerScore = 0

        self.CreateDatabase()
        self.InsertDatabase()
        self.RandomDatabase()
        self.RandomSelect()
        self.Thread = threading.Thread(target=self.Enginner(), daemon=True)
        self.Thread.start()

    def CreateDatabase(self):
        Years = time.gmtime()[0]
        Mounth = time.gmtime()[1]
        Day = time.gmtime()[2]
        Hours = time.gmtime()[3]

        LocalTime = f"{Years}-{Mounth}-{Day}-{Hours}"

        self.CURSOR.execute("CREATE TABLE IF NOT EXISTS Language(Türkçe TEXT, İngilizce TEXT, Puan TEXT, Zaman TEXT)")
        self.CON.commit()

        self.HistoryCursor.execute("CREATE TABLE IF NOT EXISTS LanguageLocal(Puan TEXT, Zaman TEXT)")
        self.History.commit()

        self.HistoryCursor.execute("INSERT INTO LanguageLocal(Puan,Zaman) VALUES(?,?)", (0, LocalTime))
        self.History.commit()

    def InsertDatabase(self):
        islem = input("Veri Eklemek İster Misiniz : 'evet/hayır' : ")
        if islem == "evet" or islem == "Evet":
            sayı = int(input("Kaç Adet Veri Eklemek İstiyorsunuz ? : "))

            while sayı:
                sayı -= 1

                Turkce = str(input("Türkçe Anlamı : "))
                English = str(input("İngilizce Anlamı : "))

                self.CURSOR.execute("INSERT INTO Language(Türkçe,İngilizce) VALUES(?,?)", (Turkce, English))
                self.CON.commit()

        elif islem == "hayır" or islem == "Hayır":
            pass

        else:
            pass

    def SelectDatabase(self):
        self.CURSOR.execute("SELECT * FROM Language")
        data = self.CURSOR.fetchall()
        return data

    def RandomDatabase(self):
        self.CURSOR.execute("SELECT Türkçe,İngilizce FROM Language ORDER BY random() LIMIT 1")
        data = self.CURSOR.fetchall()
        for i in data:
            if len(i) == 0:
                print("Veritabanında Veri Yok.")
                time.sleep(3)
                sys.exit()
            else:
                self.Türkçe = i[0]
                self.İngilizce = i[1]

        # print("Türkçe Anlam : ", self.Türkçe)
        # print("İngilizce Anlam : ",self.İngilizce)

    def RandomSelect(self):
        self.EnginnerRandom = random.randint(0, 1)

    def Hatırlat(self, MOD):
        if MOD == "Türkçe":
            tts = gTTS(f"{self.İngilizce} Anlamı. {self.Türkçe}", lang="tr")
            tts.save("Hatırlat.mp3")
            print(f"\n{self.İngilizce} : {self.Türkçe}")

        elif MOD == "İngilizce":
            tts = gTTS(f"{self.Türkçe} Anlamı. {self.İngilizce}", lang="en")
            tts.save("Hatırlat.mp3")
            print(f"\n{self.Türkçe} : {self.İngilizce}")

        TIME_OUT = str
        TRACK = "Hatırlat.mp3"

        mixer.init()
        mixer.music.load(TRACK)
        mixer.music.play()
        while (mixer.music.get_busy()):
            TIME_OUT = "\r" + str(mixer.music.get_pos())

        TIME_OUT_MATH = int(TIME_OUT) / 1000
        sleep(round(TIME_OUT_MATH, 1))
        mixer.music.unload()
        os.remove("Hatırlat.mp3")

    def Microphone(self):
        while True:
            try:
                # Türkçe
                if self.EnginnerRandom == 0:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source=source, phrase_time_limit=10, timeout=3)
                        self.Microphone_TEXT = r.recognize_google(audio, language="tr")
                        return False
                # İngilizce
                else:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source=source, phrase_time_limit=10, timeout=3)
                        self.Microphone_TEXT = r.recognize_google(audio, language="en")
                        return False
            except:
                print("\nLütfen Konuşun.")

    def Listening(self):
        if self.EnginnerRandom == 0:
            tts = gTTS(self.İngilizce, lang="en")
            tts.save("Listening.mp3")

        else:
            tts = gTTS(self.Türkçe, lang="tr")
            tts.save("Listening.mp3")

        TIME_OUT = str
        TRACK = "Listening.mp3"

        mixer.init()
        mixer.music.load(TRACK)
        mixer.music.play()
        while (mixer.music.get_busy()):
            TIME_OUT = "\r" + str(mixer.music.get_pos())

        TIME_OUT_MATH = int(TIME_OUT) / 1000
        sleep(round(TIME_OUT_MATH, 1))
        mixer.music.unload()
        os.remove("Listening.mp3")

    def Enginner(self):
        while True:

            # Finish Code
            if self.EnginnerStop == self.EnginnerScore:
                print("Başarıyla Bitirdiniz.")
                return False

            else:
                time.sleep(int(self.Sleep))
                self.RandomDatabase()
                self.RandomSelect()
                self.Listening()

                # Türkçe Konuşmak
                if self.EnginnerRandom == 0:
                    print("\nİngilizce Kelime : ", self.İngilizce.lower().strip())
                    self.Microphone()
                    print("Mikrofon Verisi : ", self.Microphone_TEXT.strip())

                    # Öğret
                    if self.Microphone_TEXT.strip() == "bilmiyorum":
                        self.Hatırlat("Türkçe")

                    elif self.Microphone_TEXT.strip() == "geçmiş":
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        DATA = self.HistoryCursor.fetchall()
                        for i in DATA:
                            print("----------------------------------------")
                            print(f"Puan : {i[0]}\t\t Tarih : {i[1]}")
                            print("----------------------------------------\n")

                    # Kelime Görüntüle
                    elif self.Microphone_TEXT.strip() == "veritabanı":
                        for i in self.SelectDatabase():
                            print("----------------------------------------")
                            print(f"Türkçe : {i[0]}\t\t İngilizce : {i[1]}")
                            print("----------------------------------------\n")

                    # Kelime Güncelle
                    elif self.Microphone_TEXT.strip() == "verilerimi güncelle" or self.Microphone_TEXT.strip() == "bilgilerimi güncelle":
                        Index = 0
                        for i in self.SelectDatabase():
                            Index += 1
                            print("----------------------------------------")
                            print(f"{Index}. SATIR -)  Türkçe : {i[0]}\t\t İngilizce : {i[1]}")
                            print("----------------------------------------\n")
                        print("Toplam Satır : ", Index)
                        print("Toplam Sütun : ", 2)

                        SATIR = int(input("Kaçıncı Satırı Güncellemek İstiyorsunuz : "))
                        SUTUN = int(input("Kaçıncı Sütunu Güncellemek İstiyorsunuz : "))
                        NEW_DATA = input("Güncellemek İstediğiniz Yeni Kelime : ")

                        Index = 0
                        for i in self.SelectDatabase():
                            Index += 1

                            if Index == int(SATIR) and SUTUN == 1:
                                ARADIGIMIZ_KELIME = i[0]
                                self.CURSOR.execute("UPDATE Language SET Türkçe = ? WHERE Türkçe = ?",
                                                    (NEW_DATA, ARADIGIMIZ_KELIME))
                                self.CON.commit()
                                print("Güncelleme Başarılı")

                            elif Index == int(SATIR) and SUTUN == 2:
                                ARADIGIMIZ_KELIME = i[1]
                                self.CURSOR.execute("UPDATE Language SET Türkçe = ? WHERE Türkçe = ?",
                                                    (NEW_DATA, ARADIGIMIZ_KELIME))
                                self.CON.commit()
                                print("Güncelleme Başarılı")

                    # Doğru
                    elif self.Microphone_TEXT.strip() == self.Türkçe.lower().strip():
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        HistoryData = self.HistoryCursor.fetchall()
                        LEN = len(HistoryData)
                        OLD_SCORE = int(HistoryData[int(LEN) - 1][0])
                        SCORE = int(HistoryData[int(LEN) - 1][0]) + 1

                        print("\nDoğru")
                        print("--------------------------")
                        print("Eski Score : ", OLD_SCORE)
                        print("Yeni Skor : ", SCORE)
                        print("--------------------------\n")

                        self.EnginnerScore += 1
                        self.HistoryCursor.execute("UPDATE LanguageLocal SET Puan = ? WHERE Puan = ?",
                                                   (SCORE, OLD_SCORE))
                        self.History.commit()

                    # Yanlış
                    else:
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        HistoryData = self.HistoryCursor.fetchall()
                        LEN = len(HistoryData)
                        OLD_SCORE = int(HistoryData[int(LEN) - 1][0])
                        SCORE = int(HistoryData[int(LEN) - 1][0]) - 1

                        print("\nYanlış")
                        print("--------------------------")
                        print("Eski Score : ", OLD_SCORE)
                        print("Yeni Skor : ", SCORE)
                        print("--------------------------\n")

                        self.EnginnerScore -= 1
                        self.HistoryCursor.execute("UPDATE LanguageLocal SET Puan = ? WHERE Puan = ?",
                                                   (SCORE, OLD_SCORE))
                        self.History.commit()

                # İngilizce Konuşmak
                else:
                    print("\nTürkçe Kelime : ", self.Türkçe.strip().lower())
                    self.Microphone()
                    print("Mikrofon Data : ", self.Microphone_TEXT)

                    # Öğret
                    if self.Microphone_TEXT.strip() == "don't know":
                        self.Hatırlat("İngilizce")

                    elif self.Microphone_TEXT.strip() == "history":
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        DATA = self.HistoryCursor.fetchall()
                        for i in DATA:
                            print("----------------------------------------")
                            print(f"Puan : {i[0]}\t\t Tarih : {i[1]}")
                            print("----------------------------------------\n")

                    # Görüntüle
                    elif self.Microphone_TEXT.strip() == "database":
                        for i in self.SelectDatabase():
                            print("----------------------------------------")
                            print(f"Türkçe : {i[0]}\t\t İngilizce : {i[1]}")
                            print("----------------------------------------\n")

                    # Güncelle
                    elif self.Microphone_TEXT.strip() == "database update" or self.Microphone_TEXT.strip() == "profile update":
                        Index = 0
                        for i in self.SelectDatabase():
                            Index += 1
                            print("----------------------------------------")
                            print(f"{Index}. SATIR -)  Türkçe : {i[0]}\t\t İngilizce : {i[1]}")
                            print("----------------------------------------\n")
                        print("Toplam Satır : ", Index)
                        print("Toplam Sütun : ", 2)

                        SATIR = int(input("Kaçıncı Satırı Güncellemek İstiyorsunuz : "))
                        SUTUN = int(input("Kaçıncı Sütunu Güncellemek İstiyorsunuz : "))
                        NEW_DATA = input("Güncellemek İstediğiniz Yeni Kelime : ")

                        Index = 0
                        for i in self.SelectDatabase():
                            Index += 1

                            if Index == int(SATIR) and SUTUN == 1:
                                ARADIGIMIZ_KELIME = i[0]
                                self.CURSOR.execute("UPDATE Language SET Türkçe = ? WHERE Türkçe = ?",
                                                    (NEW_DATA, ARADIGIMIZ_KELIME))
                                self.CON.commit()
                                print("Güncelleme Başarılı")

                            elif Index == int(SATIR) and SUTUN == 2:
                                ARADIGIMIZ_KELIME = i[1]
                                self.CURSOR.execute("UPDATE Language SET Türkçe = ? WHERE Türkçe = ?",
                                                    (NEW_DATA, ARADIGIMIZ_KELIME))
                                self.CON.commit()
                                print("Güncelleme Başarılı")

                    # Doğru
                    elif self.Microphone_TEXT.strip() == self.İngilizce.lower().strip():
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        HistoryData = self.HistoryCursor.fetchall()
                        LEN = len(HistoryData)
                        OLD_SCORE = int(HistoryData[int(LEN) - 1][0])
                        SCORE = int(HistoryData[int(LEN) - 1][0]) + 1

                        print("\nDoğru")
                        print("--------------------------")
                        print("Eski Score : ", OLD_SCORE)
                        print("Yeni Skor : ", SCORE)
                        print("--------------------------\n")

                        self.EnginnerScore += 1
                        self.HistoryCursor.execute("UPDATE LanguageLocal SET Puan = ? WHERE Puan = ?",
                                                   (SCORE, OLD_SCORE))
                        self.History.commit()

                    # Yanlış
                    else:
                        self.HistoryCursor.execute("SELECT * FROM LanguageLocal")
                        HistoryData = self.HistoryCursor.fetchall()
                        LEN = len(HistoryData)
                        OLD_SCORE = int(HistoryData[int(LEN) - 1][0])
                        SCORE = int(HistoryData[int(LEN) - 1][0]) - 1

                        print("\nYanlış")
                        print("--------------------------")
                        print("Eski Score : ", OLD_SCORE)
                        print("Yeni Skor : ", SCORE)
                        print("--------------------------\n")

                        self.EnginnerScore -= 1
                        self.HistoryCursor.execute("UPDATE LanguageLocal SET Puan = ? WHERE Puan = ?",
                                                   (SCORE, OLD_SCORE))
                        self.History.commit()


# Sleep = Soru'nun Zaman Aralığı / Score Hedef Skor.
English(Sleep=1, Score=2)
