import pandas as pd


class InformationManager:

    def __init__(self):
        self.data_df = pd.DataFrame()

    def createDataframe(self, data):
        # data is url: data dict as defined in crawler interface
        self.data_df = pd.DataFrame(data)
        self.data_df.index.name = "URL"

    def exportDataframeAsExcel(self, documentname = 'crawleroutput.xls'):  # export to DB will come later
        self.data_df.to_excel(documentname, index_label=True)

    def getDocumentListById(self, docid):
        return [("hint", "protocol", "url")]  # TODO this needs to be the list stored in the database with given id

    def getAttributeListById(self, attid):
        return [("name", "type", "patt")]  # TODO see above
