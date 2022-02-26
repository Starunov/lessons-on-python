weather_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(weather_data, 'ID:', id(weather_data))

i = 0
while i < len(weather_data):
    if weather_data[i].replace('+', '').replace('-', '').isdigit():  # '+5' -> '5'.isdigit() -> True
        if weather_data[i][0] in '+-':
            weather_data[i] = weather_data[i].zfill(3)
        else:
            weather_data[i] = weather_data[i].zfill(2)
        weather_data.insert(i, '"')
        weather_data.insert(i + 2, '"')
        i += 2
    i += 1

# string = ' '.join(weather_data) ==> эта строка будет иметь лишние пробелы между кавычками и числами
# Формирование списка без пробелов
string = []
for word in weather_data:
    if word == '"':
        continue
    elif word.isdigit() or '+' in word or '-' in word:
        string.append(f'"{word}"')
    else:
        string.append(word)

string = ' '.join(string)

print(weather_data, 'ID:', id(weather_data))
print(string)
