from random import*
class Blitz():
    def tusk_1(self,main_number):
        summ = 0
        for i in range(1,main_number):
            if main_number % i == 0:
                summ +=  i
        if summ == main_number:
            return "совершенное"
        else:
            return "несовершенное"
    def tusk_2(self):
        return [randint(-100,100) for i in range(100)]

    def tusk_3(self,listik):
        slovar = {"четные":[],"нечетные":[]}
        for i in range(len(listik)):
            if listik[i] % 2 == 0:
                slovar["четные"].append(listik[i])
            else:
                slovar["нечетные"].append(listik[i])
        return slovar
    def tusk_4(self,string):
        counter=0
        while counter != len(string):
            if string[counter].isdigit():
                string = string.replace(string[counter],"")
            else:
                counter += 1
        return string
if __name__ == "__main__":
    obj = Blitz()
    print(obj.tusk_1(6))
    print(obj.tusk_2())
    print(obj.tusk_3(obj.tusk_2()))
    print(obj.tusk_4("dsfs3tr5"))
