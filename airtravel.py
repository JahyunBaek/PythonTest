class Flight:
    class_attr = []
    def add_class_attr(self, number):
        Flight.class_attr.append(number)
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다.")
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다.")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 아닙니다.")
        self.__number = number


    def number(self):
        return 'SN060'
    

# 파이썬은 메소드 오버로딩이 없습니다.
# 아래와 같은 코드가 있다면 첫번째 show는 무시되고, 두번째 show만 유지됩니다.
class Korea:

    def __init__(self, name,population, captial):
        self.name = name
        self.population = population
        self.capital = captial

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )

    def show(self, abc):
        print('abc :', abc)