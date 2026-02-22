import requests

# Link Sumber
M3U_SRC = "https://raw.githubusercontent.com/mimipipi22/lalajo/main/playlist25"
EPG_URL = "https://raw.githubusercontent.com/karepech/Epgku/main/epg_wib_sports.xml"

def main():
    # Ambil data dari mimipipi22
    response = requests.get(M3U_SRC)
    content = response.text
    
    # Tambahkan Header EPG di baris pertama
    header = f'#EXTM3U x-tvg-url="{EPG_URL}"\n'
    
    # Proses Mapping (Contoh: Mengubah RCTI menjadi RCTI.id agar EPG jalan)
    content = content.replace('tvg-id="RCTI"', 'tvg-id="RCTI.id"')
    content = content.replace('tvg-id="SCTV"', 'tvg-id="SCTV.id"')
    # Tambahkan replace lainnya sesuai kebutuhan...

    # Simpan jadi file baru
    with open("playlist_bola.m3u", "w") as f:
        f.write(header + content)

if __name__ == "__main__":
    main()
