import pandas as pd
from DataExportInterface import *


class InformationManager:

    def __init__(self, conf):
        self.data_df = pd.DataFrame()
        self.conf = conf
        self.db = DatabaseInterface(conf)

    def createDataframe(self, data):
        # data is url: data dict as defined in crawler interface
        self.data_df = pd.DataFrame(data)
        self.data_df.index.name = "URL"

    def exportDataframeAsExcel(self, documentname = 'crawleroutput.xls'):  # export to DB will come later
        self.data_df.to_excel(documentname, index_label=True)

    def exportDataframeToDB(self, data, docid=1, attid=1):
        self.createDataframe(data)
        table = self.db.createNewDataTable(self.data_df, docid, attid)
        return table

    def getDocumentListById(self, docid):
        self.db.runStoredProcedure("getDocumentListById", (docid))
        return [("hint", "protocol", "url")]  # TODO this needs to be the list stored in the database with given id

    def getAttributeListById(self, attid):
        return [("name", "type", "patt")]  # TODO see above

    def saveAttributeData(self, attdata):
        return 1 # TODO make this the att data index id

    def getCrawlData(self, docid, attid):
        tablename = "table_" + str(docid) + '_' + str(attid)
        # TODO select * from tablename
        return
