import json
def write_to_json(data):
    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

name = input("Введите название товара: ")
price = float(input("Введите цену товара: "))

categories = ['услуги', 'авто', 'техника', 'одежда', 'мебель', 'другое']
for index, category in enumerate(categories, start=1):
    print(f"{index}. {category}")

category_index = int(input("Введите номер категории: ")) - 1
category = categories[category_index]

product = {
    'название': name,
    'цена': price,
    'категория': category
}

try:
    with open('products.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = []
data.append(product)
write_to_json(data)
print("Ваш товар добавлен в базу данных!")
print("Ждите покупки.")