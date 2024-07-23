class DZ():
    def tusk_1(self,main_list):
        second_list = []
        izgoii = []
        for i in range(len(main_list)):
            if main_list[i] not in second_list:
                second_list.append(main_list[i])
            else:
                izgoi = second_list.index(main_list[i])
                second_list.pop(izgoi)
                izgoii.append(main_list)
        return second_list
if __name__ == "__main__":
    obj = DZ()
    print(obj.tusk_1([1.1,2.3,2.3,1.1,3.5,2.1]))


