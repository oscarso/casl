from WinNum import WinNum
from CASLDB import CASuperLottoDB

w1 = WinNum(1, "MAR 10, 2023", 1, 2, 3, 4, 5, 6)
print(w1)

db = CASuperLottoDB()
db.dropTables()
db.createTables()

