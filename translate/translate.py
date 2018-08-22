import requests

FILES = ['DE.txt', 'ES.txt', 'FR.txt']


def getText(source):
    print('Getting "{}" file'.format(source))
    with open(source) as file:
        text = file.read()
        return text


def saveText(result, text):
    print('Saving "{}" file'.format(result))
    with open(result, 'w') as file:
        file.write(text)


def translate_it(source, result, srcLang, resLang='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    # Insert actual key here
    key = '0123456789'
    lang = '{}-{}'.format(srcLang, resLang)
    text = getText(source)
    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }

    print('Requesting translation for "{}" file'.format(source))
    response = requests.get(url, params=params).json()
    saveText(result, ' '.join(response.get('text', [])))


def translateFiles(fileList):
    for file in fileList:
        lang = file.split('.')[0].lower()
        resultName = 'From {} to ru.txt'.format(lang)
        translate_it(file, resultName, lang)


translateFiles(FILES)
