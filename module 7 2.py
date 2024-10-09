import io

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    position = 0
    for i, curstr in enumerate(strings):
        file.write(f"{curstr} \n")
        strings_positions[i + 1] = (position, curstr)
        position += len(curstr.encode('utf-8')) + 2

    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for key, value in result.items():
    print(f"Строка {key}: позиция - {value[0]}, значение - {value[1]}")