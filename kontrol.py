import concurrent.futures
import requests
import logging
import argparse

# Logging ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_channel(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f"Çalışıyor: {url}")
            return url
        else:
            logging.error(f"Çalışmıyor (HTTP {response.status_code}): {url}")
    except requests.RequestException as e:
        logging.error(f"Çalışmıyor: {url}, Hata: {e}")
    return None

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    urls = [line.strip() for line in lines if line.startswith('http')]

    working_channels = []
    
    # ThreadPoolExecutor kullanarak kanalları test etme
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(test_channel, urls))

    # Çalışan kanalları filtrele
    working_channels = [url for url in results if url is not None]

    with open(output_file, 'w') as file:
        for line in lines:
            if any(url in line for url in working_channels) or not line.startswith('http'):
                file.write(line)

    logging.info(f"Toplam {len(working_channels)} kanal çalışıyor.")
    logging.info(f"Çalışan kanallar {output_file} dosyasına kaydedildi.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="M3U kanallarını test eden ve çalışanları filtreleyen bir araç.")
    parser.add_argument('-i', '--input', required=True, help="Girdi M3U dosyasının yolu.")
    parser.add_argument('-o', '--output', required=True, help="Çıktı M3U dosyasının yolu.")

    args = parser.parse_args()

    main(args.input, args.output)
