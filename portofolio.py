# ============================================================
#   PORTOFOLIO - Irtiza Hanoon Kautsar
#   Jalankan: python portofolio.py
# ============================================================

def tampilkan_header():
    print("=" * 55)
    print("       PORTOFOLIO — IRTIZA HANOON KAUTSAR")
    print("=" * 55)

def tentang_saya():
    print("\n📌 TENTANG SAYA")
    print("-" * 40)
    print("  Nama    : Irtiza Hanoon Kautsar")
    print("  Status  : Pelajar")
    print("  Minat   : Teknologi, Robotika, Pemrograman")
    print("  GitHub  : github.com/irtzahanoon1234-hub")

def pengalaman():
    print("\n🏆 PENGALAMAN")
    print("-" * 40)
    pengalaman_list = [
        {
            "jabatan": "Ketua Ekskul Robotik",
            "tempat" : "MTs",
            "deskripsi": "Memimpin tim robotik, mengkoordinasikan\n"
                         "    anggota, membimbing proses belajar, dan\n"
                         "    mengorganisir kompetisi."
        }
    ]
    for i, p in enumerate(pengalaman_list, 1):
        print(f"  {i}. {p['jabatan']} — {p['tempat']}")
        print(f"     {p['deskripsi']}")

def keahlian():
    print("\n💡 KEAHLIAN")
    print("-" * 40)
    skills = [
        "Python (Tkinter, PySimpleGUI)",
        "HTML & CSS",
        "GitHub",
        "Robotika",
        "Kepemimpinan & Kerja Tim",
        "Problem Solving",
    ]
    for skill in skills:
        print(f"  ✔ {skill}")

def project():
    print("\n🚀 PROJECT")
    print("-" * 40)
    projects = [
        {
            "nama"  : "Kalkulator GUI",
            "tech"  : "Python, Tkinter",
            "desc"  : "Aplikasi kalkulator sederhana dengan tampilan\n"
                      "     GUI. Mendukung operasi +, -, *, /."
        },
        {
            "nama"  : "Image Viewer",
            "tech"  : "Python, PySimpleGUI",
            "desc"  : "Aplikasi untuk melihat gambar (PNG, JPG, GIF)\n"
                      "     dari folder yang dipilih pengguna."
        },
    ]
    for i, p in enumerate(projects, 1):
        print(f"  {i}. {p['nama']}")
        print(f"     Tech  : {p['tech']}")
        print(f"     Desc  : {p['desc']}")

def kontak():
    print("\n📬 KONTAK")
    print("-" * 40)
    print("  GitHub : github.com/irtzahanoon1234-hub")

def footer():
    print("\n" + "=" * 55)
    print("       © 2025 Irtiza Hanoon Kautsar")
    print("=" * 55 + "\n")

def menu():
    tampilkan_header()
    while True:
        print("\n📂 MENU")
        print("  [1] Tentang Saya")
        print("  [2] Pengalaman")
        print("  [3] Keahlian")
        print("  [4] Project")
        print("  [5] Kontak")
        print("  [0] Keluar")
        pilihan = input("\n  Pilih menu: ").strip()

        if pilihan == "1":
            tentang_saya()
        elif pilihan == "2":
            pengalaman()
        elif pilihan == "3":
            keahlian()
        elif pilihan == "4":
            project()
        elif pilihan == "5":
            kontak()
        elif pilihan == "0":
            footer()
            break
        else:
            print("  ⚠️  Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()
