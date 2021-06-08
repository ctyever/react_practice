from cctv_test.models import CctvDto
from common.services import CommonService
import pandas as pd


class CctvService(CommonService):

    dto = CctvDto()

    def new_model(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    def new_model_exel(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname)


