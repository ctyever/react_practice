from common.services import Printer, Reader
from common.models import FileDTO
from common.abstracts import ReaderBase


class CctvService(ReaderBase):

    file = ''

    def test1(self, payload):
        self.file = FileDTO()
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        return self.file

    def csv(self, payload):
        printer = Printer()
        reader = Reader()
        CctvService().
        printer.dframe(reader.csv(self.file))

    def xls(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.xls(file))

    def json(self):
        pass

    def new_file(self):
        pass

    # 추상클래스에 정의되지 않은 추가 메소드
    def test(self):
        pass






