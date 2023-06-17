"""Создать класс "Граф", который имеет атрибуты вершины и ребра,
 и методы добавления и удаления вершин и ребер, и проверки связности графа."""
class Graph:
    ''' tops - словарь, где key это вершина, а value список связанных с key вершин '''

    __tops = {
        #проверочный граф, удаление ребра 2,5 сделает его разъединённым
       ''' 1: [2, 4, 3],
        2: [1, 3, 5],
        3: [2, 4, 1],
        4: [3, 1],
        5: [2, 6, 7],
        6: [5, 8],
        7: [5, 8],
        8: [6, 7]'''
    }


    def graph_print(self):
        print(self.__tops)


    def add_top(self, top_name): # добавляет вершину без связей
        if top_name not in self.__tops:
            self.__tops.update({top_name: []})
        print('Вершина уже существует')

    def add_rib(self, top_1, top_2): #добавляет связь между вершинами,а при необходимости и сами вершины

        if top_1 not in self.__tops:
            print("Вершина", top_1, "будет добавлена в граф")
            self.add_top(top_1)

        if top_2 not in self.__tops:
            print("Вершина", top_2, "будет добавлена в граф")
            self.add_top(top_2)

        if top_2 not in self.__tops[top_1]:
            self.__tops[top_1].append(top_2)
            self.__tops[top_2].append(top_1)
        else:
            print("Данное ребро уже существует")

    def delete_rib(self, top_1, top_2):#удаление ребра
        if top_1 in self.__tops:
            if top_2 in self.__tops:
                if top_1 in self.__tops[top_2]:
                    self.__tops[top_1].remove(top_2)
                    self.__tops[top_2].remove(top_1)
                else:
                    print("Ребро не существует")
            else:
                print("Вершины", top_2, "не существует")
        else:
            print("Вершины", top_1, "не существует")

    def delete_top(self, top):#даление вершины
        if top in self.__tops:
            for i in self.__tops[top]:#удаление ребер со стороны связанных вершин
                self.__tops[i].remove(top)
            self.__tops.pop(top, None)
        else:
            print("Вершины", top, "не существует")

    def __check_top(self, top, check_list=[]):
        """рекурсивная функция возвращает список(check_list) всех доступных вершин для вершины top,
        проходит по всем связанным с top вершинами и записывает их в check_list"""
        check_list.append(top)
        for i in self.__tops[top]:
            if i not in check_list:
                self.__check_top(i, check_list)
        return check_list

    def connectivity_check(self):#проверка на связность графа
        top = next(iter(self.__tops.keys()))#задаём стартовую точку для check_top

        check_list = self.__check_top(top)

        if len(check_list) == len(self.__tops):#сравнение кол-ва доступных для top точек с  общим их кол-ом в графе
            print('граф связный')
        else:
            print("граф разъединённый")


g = Graph()

g.connectivity_check()



