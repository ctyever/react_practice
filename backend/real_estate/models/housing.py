from real_estate.models.dataset import Dataset
import pandas as pd


class Housing(object):

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\project\\backend\\real_estate\\data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname, engine='python', encoding='euc-kr' )







