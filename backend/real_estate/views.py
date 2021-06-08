from real_estate.services import HousingService
from real_estate.models import HousingDTO


class HousingApi(object):

    @staticmethod
    def print_this(this):
        print(f'Housing 의 type \n {type(this)} 이다')
        print(f'Train 의 column \n {this.columns} 이다')
        print(f'Train 의 상위5개 행 \n {this.head()} 이다')
        print(f'Train 의 null 의 갯수 \n {this.isnull().sum()}개')

    @staticmethod
    def main():

        dto = HousingDTO()
        util = HousingService()
        while 1:
            menu = input('0.Exit 1.데이터프레임생성\n'
                         '2.구군에서 None삭제\n'
                         '3.')

            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model('housing')



