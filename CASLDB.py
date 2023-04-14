import sqlite3

from WinNum import WinNum
from StatOrder import StatOrder


class CASuperLottoDB:
    dbname = 'lotto.db'
    dbconn = None

    # constructor
    def __init__(self):
        CASuperLottoDB.dbconn = sqlite3.connect(CASuperLottoDB.dbname)

    # destructor
    def __del__(self):
        CASuperLottoDB.dbconn.close()

    # create and init DB
    def createDB(self, datafile):
        self.datafile = datafile
        f = open(self.datafile, 'r')
        Rows = f.readlines()
        for r in Rows:
            print(r)

    def dropTables(self):
        dbc = CASuperLottoDB.dbconn.cursor()
        dbc.execute(WinNum.SQL_DROP_TABLE)
        dbc.execute(StatOrder.SQL_DROP_TABLE)
        CASuperLottoDB.dbconn.commit()
        dbc.close()

    def createTables(self):
        dbc = CASuperLottoDB.dbconn.cursor()
        dbc.execute(WinNum.SQL_CREATE_TABLE)
        dbc.execute(StatOrder.SQL_CREATE_TABLE)
        CASuperLottoDB.dbconn.commit()
        dbc.close()
