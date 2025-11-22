<<<<<<< HEAD
# # # # # # # # # # # # akun_member = [
# # # # # # # # # # # #     {
# # # # # # # # # # # #         "id": "",
# # # # # # # # # # # #         "username": "a",
# # # # # # # # # # # #         "password": "b"
# # # # # # # # # # # #     },
# # # # # # # # # # # #     {
# # # # # # # # # # # #         "id": "1",
# # # # # # # # # # # #         "username": "user1",
# # # # # # # # # # # #         "password": "pass1"
# # # # # # # # # # # #     }
# # # # # # # # # # # # ]
# # # # # # # # # # # # print([i["username"]for i in akun_member])
=======
# # # # # # # # # # # akun_member = [
# # # # # # # # # # #     {
# # # # # # # # # # #         "id": "",
# # # # # # # # # # #         "username": "a",
# # # # # # # # # # #         "password": "b"
# # # # # # # # # # #     },
# # # # # # # # # # #     {
# # # # # # # # # # #         "id": "1",
# # # # # # # # # # #         "username": "user1",
# # # # # # # # # # #         "password": "pass1"
# # # # # # # # # # #     }
# # # # # # # # # # # ]
# # # # # # # # # # # print([i["username"]for i in akun_member])

# # # # # # # import tkinter as tk
# # # # # # # from tkinter import messagebox

# # # # # # # def login():..
# # # # # # #     user = entry_user.get()
# # # # # # #     pw = entry_pw.get()
# # # # # # #     if user == "jovan" and pw == "123":
# # # # # # #         messagebox.showinfo("Login", "Berhasil!")
# # # # # # #     else:
# # # # # # #         messagebox.showerror("Login", "Username/Password salah.")

# # # # # # # root = tk.Tk()
# # # # # # # root.title("Login")

# # # # # # # tk.Label(root, text="Username").pack()
# # # # # # # entry_user = tk.Entry(root)
# # # # # # # entry_user.pack()

# # # # # # # tk.Label(root, text="Password").pack()
# # # # # # # entry_pw = tk.Entry(root, show="*")
# # # # # # # entry_pw.pack()

# # # # # # # tk.Button(root, text="Login", command=login).pack()
# # # # # # # root.mainloop()

# # # # # # # import tkinter as tk
# # # # # # # from tkinter import ttk
# # # # # # # import time

# # # # # # # # Splash screen
# # # # # # # splash = tk.Tk()
# # # # # # # splash.overrideredirect(True)  # hilangkan border
# # # # # # # splash.geometry("400x200+500+300")
# # # # # # # tk.Label(splash, text="GwehMauJalan", font=("Arial", 24)).pack(pady=40)
# # # # # # # progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="determinate")
# # # # # # # progress.pack(pady=20)

# # # # # # # for i in range(101):
# # # # # # #     progress['value'] = i
# # # # # # #     splash.update()
# # # # # # #     time.sleep(0.03)

# # # # # # # splash.destroy()

# # # # # # # # Main window
# # # # # # # root = tk.Tk()
# # # # # # # root.title("GwehMauJalan")
# # # # # # # tk.Label(root, text="Selamat datang!", font=("Arial", 18)).pack(pady=50)
# # # # # # # root.mainloop()
>>>>>>> 48092e5df9549071acff60d447dc5e2c38dbc016

# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import messagebox

# # # # # # # # def login():
# # # # # # # #     user = entry_user.get()
# # # # # # # #     pw = entry_pw.get()
# # # # # # # #     if user == "jovan" and pw == "123":
# # # # # # # #         messagebox.showinfo("Login", "Berhasil!")
# # # # # # # #     else:
# # # # # # # #         messagebox.showerror("Login", "Username/Password salah.")

# # # # # # # # root = tk.Tk()
# # # # # # # # root.title("Login")

# # # # # # # # tk.Label(root, text="Username").pack()
# # # # # # # # entry_user = tk.Entry(root)
# # # # # # # # entry_user.pack()

# # # # # # # # tk.Label(root, text="Password").pack()
# # # # # # # # entry_pw = tk.Entry(root, show="*")
# # # # # # # # entry_pw.pack()

# # # # # # # # tk.Button(root, text="Login", command=login).pack()
# # # # # # # # root.mainloop()

# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import ttk
# # # # # # # # import time

# # # # # # # # # Splash screen
# # # # # # # # splash = tk.Tk()
# # # # # # # # splash.overrideredirect(True)  # hilangkan border
# # # # # # # # splash.geometry("400x200+500+300")
# # # # # # # # tk.Label(splash, text="GwehMauJalan", font=("Arial", 24)).pack(pady=40)
# # # # # # # # progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="determinate")
# # # # # # # # progress.pack(pady=20)

# # # # # # # # for i in range(101):
# # # # # # # #     progress['value'] = i
# # # # # # # #     splash.update()
# # # # # # # #     time.sleep(0.03)

# # # # # # # # splash.destroy()

# # # # # # # # # Main window
# # # # # # # # root = tk.Tk()
# # # # # # # # root.title("GwehMauJalan")
# # # # # # # # tk.Label(root, text="Selamat datang!", font=("Arial", 18)).pack(pady=50)
# # # # # # # # root.mainloop()

# # # # # # # # # import tkinter as tk
# # # # # # # # # from tkinter import messagebox

# # # # # # # # # def pilih_rute():
# # # # # # # # #     pilihan = listbox.get(listbox.curselection())
# # # # # # # # #     messagebox.showinfo("Pilihan Rute", f"Kamu memilih: {pilihan}")

# # # # # # # # # root = tk.Tk()
# # # # # # # # # root.title("Pilih Rute")

# # # # # # # # # tk.Label(root, text="Pilih rute perjalanan:").pack(pady=10)

# # # # # # # # # listbox = tk.Listbox(root)
# # # # # # # # # listbox.pack()
# # # # # # # # # for r in ["Balikpapan-Samarinda", "Samarinda-Bontang", "Balikpapan-Bontang"]:
# # # # # # # # #     listbox.insert(tk.END, r)

# # # # # # # # # tk.Button(root, text="Pilih", command=pilih_rute).pack(pady=10)

# # # # # # # # # root.mainloop()

# # # # # # # # import inquirer
# # # # # # # # login = [
# # # # # # # #         inquirer.List("login",
# # # # # # # #                       message="Pilih menu",
# # # # # # # #                      choices=[
# # # # # # # #                          "Login",
# # # # # # # #                          "Registrasi",
# # # # # # # #                          "Keluar"
# # # # # # # #                      ]
# # # # # # # #                      )
                      
# # # # # # # #     ]
# # # # # # # # jawab = inquirer.prompt(login)
# # # # # # # # print(jawab["login"])

# # # # # # # # import json
# # # # # # # # from file_data.datajson import baca_data

# # # # # # # # data = baca_data()
# # # # # # # # a = data["member"]
# # # # # # # # for i in a:
# # # # # # # #     print(i["username"])
# # # # # # # # import inquirer
# # # # # # # # menu_awal = [
# # # # # # # #         inquirer.List("admin_menu",
# # # # # # # #                       message = "Pilih Salah Satu Menu Yang Tersedia",
# # # # # # # #                       choices = [
# # # # # # # #                           "1. Membuat Rute Perjalanan Baru",
# # # # # # # #                           "2. Melihat Semua Rute Perjalanan",
# # # # # # # #                           "3. Menghapus Rute Perjalanan",
# # # # # # # #                           "4. Melihat dan Menangani Laporan Pengguna Tentng Rute",
# # # # # # # #                           "5. Melihat dan Menghapus Review Pengguna",
# # # # # # # #                           "6. Mengelola Akun Pengguna",
# # # # # # # #                           "7. Logout"
# # # # # # # #                       ]
# # # # # # # #                     )   
# # # # # # # #     ]
# # # # # # # # jawab =inquirer.prompt(menu_awal)
# # # # # # # # print(jawab["admin_menu"][0])
       
# # # # # # # for i in range (5,0,1):
# # # # # # #     print(i)

# # # # # # import inquirer
# # # # # # q = [inquirer.List("a", message="Tes", choices=["A","B","C"])]
# # # # # # print(inquirer.prompt(q))

# # # # # for i in range(0,5):
# # # # #     print(i)

# # # # import sys
# # # # import time

# # # # def spinner_bola(durasi=3):
# # # #     spinner = ["◐", "◓", "◑", "◒"]
# # # #     akhir = time.time() + durasi

# # # #     while time.time() < akhir:
# # # #         for simbol in spinner:
# # # #             sys.stdout.write(f"\rMemuat {simbol} ")
# # # #             sys.stdout.flush()
# # # #             time.sleep(0.1)

# # # #     print("\rSelesai!     ")

# # # # spinner_bola(durasi = 3)

# # # import sys
# # # import time

# # # def spinner_besar(durasi=3):
# # #     frames = [
# # #         """ 
# # #    █████   
# # #  ██     ██
# # #  █       █
# # #  ██     ██
# # #    █████   
# # #         """,
# # #         """ 
# # #      ██    
# # #    ████   
# # #  ██  ██   
# # #    ████   
# # #      ██    
# # #         """,
# # #         """ 
# # #    █████   
# # #  ██     ██
# # #  █       █
# # #  ██     ██
# # #    █████   
# # #         """,
# # #         """ 
# # #     ██     
# # #    ████   
# # #    ██ ██  
# # #    ████   
# # #     ██     
# # #         """
# # #     ]

# # #     end = time.time() + durasi

# # #     while time.time() < end:
# # #         for f in frames:
# # #             sys.stdout.write("\r" + f)
# # #             sys.stdout.flush()
# # #             time.sleep(0.2)
# # #             sys.stdout.write("\033[F" * 7)  # naik 7 baris agar animasi overwrite


# # # spinner_besar(durasi=3)



# # a = ["1",'2','3','4','8','9','10','60','8','9','765']
# # print(sorted(a))
# x = {
#     "y" : "Gak error"
# }
# print(f"test {x["y"]}")

data = {"perjalanan_terakhir": {}}

username = "alvaro"
kota = "Samarinda"

data["perjalanan_terakhir"][username] = kota

print(data)
