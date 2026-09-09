class Pracownik:
    def __init__(self, imie, pensja):
        self.imie = imie
        self.pensja = pensja
        
    def podwyzka(self, procent):
        self.pensja += self.pensja * (procent / 100)

# Проверка (эффект конечный):
p1 = Pracownik("Ola", 5000)
p1.podwyzka(10)
print(p1.pensja)
# Выведет: 5500.0


#1. Конструктор (⁠__init__⁠): принимает имя и зарплату, сохраняя их в поля ⁠self.imie⁠ и ⁠self.pensja⁠.
#2. Метод ⁠podwyzka⁠: рассчитывает прибавку как процент от текущей зарплаты и прибавляет её к ⁠self.pensja⁠.
#3. Создание объекта и вызов: объект ⁠p1⁠ инициализируется значением ⁠5000⁠, после чего метод увеличивает её на 10%, делая значение постоянным (персистентным в рамках объекта), что подтверждается выводом ⁠print(p1.pensja)⁠.
