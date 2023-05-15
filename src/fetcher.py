from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import os


def fetch_verse_list(url, browser):
    browser.get(url)
    wait = WebDriverWait(browser, 20)

    try:
        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "SanSloka")))
        result = browser.execute_script("""
            function fetchVerses(verseCount) {
            const ps = document.querySelectorAll("p");
            const verses = [];
            let current = 0;
            ps.forEach((p) => {
                if (current <= verseCount) {
                    try {
                        if (p.className == "verloc") {
                            let anchor = p.firstElementChild;
                            if (anchor.tagName == "EM") anchor = anchor.firstElementChild;
                            current = parseInt(anchor.name.substr(5));
                            verses[current - 1] = {
                                SanSloka: "",
                                pratipada: "",
                                tat: "",
                                comment: "",
                            };
                        } else if (current > 0 && p.innerText.trim() !== "") {
                            verses[current - 1][p.className] += p.innerText + "\\n";
                        }
                    } catch (error) {
                        console.log("Something went wrong");
                    }
                }
            });
            return verses;
        }
        function getVerseCounts() {
            const cells = document.querySelectorAll("table tr td a");
            const lastVerse = cells[cells.length - 1].href.split("#")[1];
            return parseInt(lastVerse.substr(5));
        }
        const verseList = fetchVerses(getVerseCounts());
        return JSON.stringify(verseList);
        """)
    except:
        result = '{"status": "Not Found"}'

    return result


def create_url_list(kanda, sarga_count):
    BASE_URL = 'https://www.valmikiramayan.net/utf8/'
    URL_STRUCTS = {
        'BALA': 'baala/sarga$i/balasans$i.htm',
        'AYODHYA': 'ayodhya/sarga$i/ayodhyasans$i.htm',
        'ARANYA': 'aranya/sarga$i/aranyasans$i.htm',
        'KISHKINDHA': 'kish/sarga$i/kishkindhasans$i.htm',
        'SUNDARA': 'sundara/sarga$i/sundarasans$i.htm',
        'YUDDHA': 'yuddha/sarga$i/yuddhasans$i.htm'
    }

    urls = []
    for i in tqdm(range(1, sarga_count + 1)):
        url = BASE_URL + URL_STRUCTS[kanda].replace('$i', str(i))
        urls.append(url)
    return urls


def save_to_file(file_name, content):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, f'book/{file_name}.json')
    with open(file_path, 'a', encoding='utf-8') as outfile:
        outfile.write(content)


def fetch_verses(sarga_list, save_file_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ssl-protocol=any")
    chrome_options.add_argument("--ignore-ssl-errors=true")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--silent")
    browser = webdriver.Chrome(options=chrome_options)

    save_to_file(save_file_name, '[\n')
    sarga_count = 0
    for sarga in tqdm(sarga_list):
        sarga_count += 1
        result = fetch_verse_list(sarga, browser)
        save_to_file(save_file_name, result)
        if (sarga_count < len(sarga_list)): save_to_file(save_file_name, ',\n')
    save_to_file(save_file_name, '\n]')

    browser.quit()
    print("all saved...")


def main():
    KANDA_LIST = {
        'BALA': 77,
        'AYODHYA': 119,
        'ARANYA': 75,
        'KISHKINDHA': 67,
        'SUNDARA': 68,
        'YUDDHA': 128
    }
    for kanda in KANDA_LIST:
        FILE_NAME = f'VALMIKI_RAMAYANA__{kanda}_KANDA'
        SARGA_COUNT = KANDA_LIST[kanda]

        print(f'$ SELCTED -> {kanda} KANDA ({SARGA_COUNT})')
        print(f'\tConstructing URLS:\n')
        sarga_list = create_url_list(kanda, SARGA_COUNT)
        print(f'\tFetching Sargas:')
        fetch_verses(sarga_list=sarga_list, save_file_name=FILE_NAME)

if __name__ == '__main__':
    main()
