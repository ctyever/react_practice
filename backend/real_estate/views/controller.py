from real_estate.models.housing import Housing
from real_estate.models.dataset import Dataset


class Controller(object):

    @staticmethod
    def main():

        while 1:
            menu = input('0.Exit 1.모델생성 2.DF')

            if menu == '1':
                dataset = Dataset()
                housing = Housing()
                dataset.housing = housing.new_model('apartment.csv')
                print('*' * 100)
                print(f'Housing의 type \n {type(dataset.housing)} 이다')

                print(f'Housing 의 column \n {dataset.housing.columns} 이다')
                print(f'Housing 의 상위5개 행 \n {dataset.housing.head()} 이다')
                print(f'Housing 의 null 의 갯수 \n {dataset.housing.isnull().sum()}개')

                print('*' * 100)


Controller.main()















