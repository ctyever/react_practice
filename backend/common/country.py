class Country(object):
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('국가 클래스의 메소드입니다')

class Korea(Country):

    def show_name(self):
        print(f'국가 이름은 {self.name} 입니다')

def execute():
    k = Korea()
    k.name = '대한민국'
    k.show_name()

execute()