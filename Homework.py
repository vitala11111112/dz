class HomeWork():
    def tusk_1(self):
        tablitsa = []
        for i in range(1,10):
            for j in range(1,10):
                print(i,"*",j,"==", i*j)
            print("")
         
    def tusk_2(self,main_number):
        counter = 2
        number = 4
        divider = 2
        divider_counter = 0
        while counter != main_number:
            while True:
                while divider != number - 1:
                    if number % divider == 0:
                        number += 1
                        divider = 2
                        break
                    elif divider_counter == 0 and divider == number - 2:
                        print(number)
                        counter += 1
                        number += 1 
                        divider = 2
                        break
 


if __name__ == "__main__":
    obj = HomeWork()
    obj.tusk_1()
    obj.tusk_2(3)
    