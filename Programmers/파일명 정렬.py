import re


def solution(files):
    answer = []
    file_info = list()
    for file in files:
        number = re.findall('[0-9]+', file)[0]
        print(number)
        print(int(number))
        head = file.split(number)[0]
        head_key = re.sub("[\t]|[\.-]+", '', head)
        file_info.append({'head': head_key.lower(), 'number': int(number), 'full': file})

    sortedFile = sorted(file_info, key=lambda x: (x['head'], x['number']))
    answer = [file_name['full'] for file_name in sortedFile]
    print(answer)
    return answer

files = ['foo010bar020.zip', "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", 'MUZI01.zip', 'muzi1.png', 'muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT']
solution(files)
