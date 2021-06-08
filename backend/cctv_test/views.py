from cctv_test.services import CctvService
from cctv_test.models import CctvDto


class CctcApi(object):


    @staticmethod
    def main():

        dto = CctvDto()
        service = CctvService()

        while 1:

            menu = input('1.csv 2.excel')

            if menu == '1':
                dto.dframe = service.new_model(input('파일명 입력'))
                service.print_dframe(dto.dframe)
            if menu == '2':
                dto.dframe = service.new_model_exel(input('파일명 입력'))
                service.print_dframe(dto.dframe)

CctcApi.main()

