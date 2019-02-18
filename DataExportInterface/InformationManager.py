import pandas as pd


class InformationManager:

    def __init__(self):
        self.data_df = pd.DataFrame()

    def createDataframe(self, data):
        # data is url: data dict as defined in crawler interface
        self.data_df = pd.DataFrame(data)

    def exportDataframeAsExcel(self, documentname = 'crawleroutput.xls'):  # export to DB will come later
        self.data_df.to_excel(documentname)
