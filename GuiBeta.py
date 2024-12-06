import customtkinter as ctk
from tkinter import filedialog
import concurrent.futures
import requests
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def test_channel(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Çalışıyor: {url}"
        else:
            return f"Çalışmıyor (HTTP {response.status_code}): {url}"
    except requests.RequestException as e:
        return f"Çalışmıyor: {url}, Hata: {e}"

def process_files(input_file, output_file, progress_label, log_textbox):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    urls = [line.strip() for line in lines if line.startswith('http')]

    working_channels = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i, result in enumerate(executor.map(test_channel, urls), 1):
            log_textbox.insert(ctk.END, result + "\n")
            log_textbox.see(ctk.END)
            progress_label.configure(text=f"İlerleme: {i}/{len(urls)}")
            if "Çalışıyor" in result:
                working_channels.append(result.split(": ")[1])
    with open(output_file, 'w') as file:
        for line in lines:
            if any(url in line for url in working_channels) or not line.startswith('http'):
                file.write(line)

    progress_label.configure(text=f"Tamamlandı! {len(working_channels)} kanal çalışıyor.")
def main_gui():
    app = ctk.CTk()
    app.title("M3U Kanal Test Aracı")
    app.geometry("600x400")

    def select_input_file():
        input_path.set(filedialog.askopenfilename(filetypes=[("M3U Files", "*.m3u")]))
    
    def select_output_file():
        output_path.set(filedialog.asksaveasfilename(defaultextension=".m3u", filetypes=[("M3U Files", "*.m3u")]))

    def start_processing():
        input_file = input_path.get()
        output_file = output_path.get()
        if not input_file or not output_file:
            progress_label.configure(text="Lütfen tüm dosya yollarını seçin!")
            return
        progress_label.configure(text="İşlem başlatıldı...")
        log_textbox.delete(1.0, ctk.END)
        process_files(input_file, output_file, progress_label, log_textbox)
    input_path = ctk.StringVar()
    ctk.CTkLabel(app, text="Girdi Dosyası:").pack(pady=5)
    ctk.CTkEntry(app, textvariable=input_path, width=400).pack(pady=5)
    ctk.CTkButton(app, text="Dosya Seç", command=select_input_file).pack(pady=5)
    output_path = ctk.StringVar()
    ctk.CTkLabel(app, text="Çıktı Dosyası:").pack(pady=5)
    ctk.CTkEntry(app, textvariable=output_path, width=400).pack(pady=5)
    ctk.CTkButton(app, text="Dosya Seç", command=select_output_file).pack(pady=5)
    ctk.CTkButton(app, text="Başlat", command=start_processing).pack(pady=20)
    progress_label = ctk.CTkLabel(app, text="Durum: Bekleniyor...")
    progress_label.pack(pady=5)
    log_textbox = ctk.CTkTextbox(app, width=500, height=150)
    log_textbox.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main_gui()
