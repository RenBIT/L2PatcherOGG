import glob #Подключим библеатеку
count = 0
for file in glob.iglob("*.ogg"):#Ищем все файлы с расширением ogg в текущем каталоге
 with open(file, 'rb+') as fn:#Открываем файл
  fn.write(b'\x4f\x67\x67\x53')#Переписываем байты на свои
  print(file)#Выводим имя файл в консоль
  count += 1
print("\nПреобразовано  файлов:", count)#При завершение предложим нажать ENTER для выхода
input("\nНажмите ENTER для выхода!")