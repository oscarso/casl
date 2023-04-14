class WinNum:

    SQL_DROP_TABLE = "DROP TABLE IF EXISTS WinNum;"
    SQL_CREATE_TABLE = """ CREATE TABLE WinNum (
                dnum  INTEGER NOT NULL UNIQUE,
                ddate TEXT NOT NULL,
                n1    TEXT NOT NULL,
                n2    TEXT NOT NULL,
                n3    TEXT NOT NULL,
                n4    TEXT NOT NULL,
                n5    TEXT NOT NULL,
                s     TEXT NOT NULL,
                PRIMARY KEY("dnum")
            ); """

    def __init__(self, dnum, ddate, n1, n2, n3, n4, n5, s):
        self.dnum = dnum
        self.ddate = ddate
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.s = s
