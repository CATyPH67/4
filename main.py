import re


def read_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as file_object:
        lines = file_object.read()
    # text = list(map(str, re.split('. | |, |: |! | - |\n', lines)))
    text = re.sub(r'[^\w.]', ' ', lines)
    words = text.split()
    return words


def write_file(filename: str, data: list):
    with open(filename + ".txt", 'w', encoding='utf-8') as file_object:
        file_object.write(data.__str__())


def text_to_dates(text: list):
    dates = list()

    months = [
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря"
    ]

    for i in range(len(text)):
        if len(text[i]) == 10:
            if text[i][:2].isdigit() and text[i][3:5].isdigit() and text[i][6:].isdigit() \
                    and text[i][2] == '.' and text[i][5] == '.':
                dates.append(text[i])
                continue
        if i + 1 < len(text):
            if text[i].isdigit() and text[i + 1].lower() in months:
                date = text[i] + ' ' + text[i + 1]
                if i + 2 < len(text):
                    if text[i + 2].isdigit():
                        date += ' ' + text[i + 2]
                dates.append(date)

    return dates


def main():
    words = read_file("input2.txt")
    dates = text_to_dates(words)
    write_file("output", dates)


if __name__ == '__main__':
    main()
