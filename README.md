# Valmiki Ramayana Reader

A python GUI reader for Valmiki Ramayana with Sanskrit Slokas and English meanings with Sloka **breakdowns**.

## Preface

Ramayana is one of the epics and a part of history of Sanatana Dharma (Hindu religion). It was written by sage Valmiki who was there during Ramayana. You will find that Ramayana has 7 kandas but the actual Valmiki Ramayana consists of **6 Kandas**. The 7th Kanda was added later so it's a matter of debate that whether the incidents in the 7th Kanda (uttara Kanda) is true or not.

So I present you *the **original** Valmiki Ramayana with Sanskrit Slokas, Meanings and more...*

## Installation

1. First download / clone the repository

   ```terminal
   got clone https://github.com/hind-sagar-biswas/Ramayana.git
   ```

2. install all the packages from `requirements.txt`
3. run the following command in terminal

   ```terminal
   pyinstaller --noconsole --icon="./src/images/logo.ico" --add-data "./src/images;images" --add-data "./src/fonts;fonts" --add-data "./src/book;book" "./src/main.py"
   ```

4. After the installation finishes, you'll find the executable file in `.\dist\main\` directory as `main.exe`

## Used Packages

1. PyQt5
2. selenium
3. pyttsx3

### Disclaimer

The contents (slokas, meanings etc.) are taken from [valmikiramayan.net](https://valmikiramayan.net)
