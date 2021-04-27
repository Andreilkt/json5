import json

# Открываем файл для записи JSON дампа
fp = open('tempfile.json', mode='w');

# Объект, который мы будем записывать
obj = {
  "propList": [
    {
      "propStr": "str",
      "propInt": 5,
      "propBool": False
    }
  ],
  "propEnum": "camelCase"
}

# Сермализуем объект в JSON формате
json.dump(obj, fp)

# Закрываем файл и делаем контрольное чтение
fp.close()
fp = open('tempfile.json', mode='r');

# Десериализуем из формата JSON
obj_new = json.load(fp)
print(obj_new)

