from real_estate.views.controller import Controller


if __name__=='__main__':

    controller = Controller()

    while 1:

         menu = input('1. data visualization')

         if menu == '1':

             controller.preprocess('apartment.csv')


