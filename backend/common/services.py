from common.abstracts import PrinterBase, ReaderBase
import pandas as pd
import json


class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. Target 의 type \n {type(this)} ')
        print(f'2. Target 의 column \n {this.columns} ')
        print(f'3. Target 의 상위 1개 행\n {this.head()} ')
        print(f'4. Target 의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)


class Reader(ReaderBase):

    def new_file(self, file):
        return file.context + file.fname

    def csv(self, file):
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file):
        return pd.read_excel(f'{self.new_file(file)}.xls', encoding='UTF-8', header='header', usecols='usecols')

    def json(self, file):
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))




