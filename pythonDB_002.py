import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def simpan_data(nama_siswa,biologi, fisika, inggris):
    conn = sqlite3.connect("prediksinilai_prodi.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa varchar (50),
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER
        )
    ''')

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris)
        VALUES (?, ?, ?, ?)
    ''', (nama_siswa,biologi, fisika, inggris))

    conn.commit()
    conn.close()

guntur = tk.Tk()
guntur.configure(background='black')
guntur.geometry('500x500')

guntur.title('Aplikasi Prediksi Prodi Pilihan')

#make Label
ui = tk.Frame(guntur)
ui.pack(padx=10,fill='x',expand=True)

inputLabel = tk.Label(ui,text='Aplikasi Prediksi Jurusan Berdasarkan Nilai')
inputLabel.pack(padx=10,pady=10,fill='x',expand=True)

#membuat input nama siswa
labelinputsiswa=ttk.Label(ui,text='Nama Siswa')
labelinputsiswa.pack(padx=10,pady=5,fil='x',expand=True)

entryinputsiswa =ttk.Entry(ui)
entryinputsiswa.pack(padx=10,pady=5,fill='x',expand=True)

##membuat input nilai biologi
labelinputbio=ttk.Label(ui,text='Nilai Biologi')
labelinputbio.pack(padx=10,pady=5,fil='x',expand=True)

entryinputbio =ttk.Entry(ui)
entryinputbio.pack(padx=10,pady=5,fill='x',expand=True)

#membuat input nilai fisika
labelinputfsk=ttk.Label(ui,text='Nilai Fisika')
labelinputfsk.pack(padx=10,pady=5,fil='x',expand=True)

entryinputfsk =ttk.Entry(ui)
entryinputfsk.pack(padx=10,pady=5,fill='x',expand=True)

#membuat input nilai bahasa inggris
labelinputigr=ttk.Label(ui,text="Nilai Bahasa Inggris")
labelinputigr.pack(padx=10,pady=5,fill='x',expand=True)

entryinputigr =ttk.Entry(ui)
entryinputigr.pack(padx=10,pady=5,fill='x',expand=True)
def prediksi(biologi, fisika, inggris):
    nilai_Maximal = max(biologi, fisika, inggris)

    if nilai_Maximal == biologi:
        return "Kedokteran"
    elif nilai_Maximal == fisika:
        return "Teknik"
    elif nilai_Maximal == inggris:
        return "Bahasa"

def klikbutton():
    siswa = entryinputsiswa.get()
    biologi = entryinputbio.get()
    fisika = entryinputfsk.get()
    inggris = entryinputigr.get()

    if not siswa or not biologi or not fisika or not inggris:
        messagebox.showerror("Error", "Masukkan Semua Nilainya.")
        return

    simpan_data(siswa, biologi, fisika, inggris)

    prediksiprogram = prediksi(int(biologi), int(fisika), int(inggris))
    messagebox.showinfo("Hasil prediksi", f"Hasil Prediksi Prodi pilihan berdasarkan nilai adalah {prediksiprogram}")

button = ttk.Button(ui,text='Cek Prediksi',command=klikbutton)
button.pack(padx=10,pady=5,fill='x',expand=True)


guntur.mainloop()