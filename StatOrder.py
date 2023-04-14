class StatOrder:

    SQL_DROP_TABLE = " DROP TABLE IF EXISTS StatOrder; "
    SQL_CREATE_TABLE = """ CREATE TABLE StatOrder (
                seqkey TEXT NOT NULL UNIQUE,
                onum   INTEGER NOT NULL,
                next   TEXT NOT NULL,
                freq   INTEGER NOT NULL,
                PRIMARY KEY("seqkey")
            ); """

    def __init__(self, seqkey, onum, next, freq):
        self.seqkey = seqkey
        self.onum = onum
        self.next = next
        self.freq = freq
