import sqlite3

class BasePixhos():
    def __init__(self):
        self.con = sqlite3.connect("base.db")
        self.cur = self.con.cursor()

        self.__create_tables()
        # self.__insert_default()
    
    def __create_tables(self) -> None:
        self.cur.execute("""CREATE TABLE IF NOT EXISTS pixhos (
            id	INTEGER NOT NULL,
            name	TEXT NOT NULL,
            city	TEXT NOT NULL,
            key_type	TEXT NOT NULL,
            key	TEXT NOT NULL,
            amount	TEXT,
            reference	TEXT,
            payload TEXT,
            PRIMARY KEY(id AUTOINCREMENT)
        )""")

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS config (
            prt_default	TEXT,
            qrcode_size	INTEGER DEFAULT 7,
            qrcode_border	INTEGER DEFAULT 4
        )""")

    def __insert_default(self) -> None:
        # self.cur.execute("INSERT INTO config (prt_default, qrcode_border, qrcode_size) VALUES ('Fax', 4, 7)")
        self.cur.execute("INSERT INTO pixhos (id, name, city, key_type, key, amount, reference, payload) VALUES (null, '', '', '', '', null, null, null)")
        self.con.commit()

    @property
    def config(self):
        res = self.__select_one('config')
        if res != None:
            if len(res) > 0:
                c = {
                    'prt_default': res[0],
                    'qrcode_size': res[1],
                    'qrcode_border': res[2],
                    }
                return c;
        return None
    
    @property
    def pixhos(self):
        res = self.__select_all('pixhos')

        return list(map(
                lambda x: {
                    'id':x[0],
                    'name':x[1],
                    'city':x[2],
                    'key_type':x[3],
                    'key':x[4],
                    'amount':x[5],
                    'reference':x[6],
                    'payload':x[7],
                },
                res
            ))

    def insert_pixhos(self, name: str, city: str, key_type:str ,key:str ,payload:str = None, amount: str = None, reference: str = None):

        payload = "" if payload == None else payload
        amount = "0,00" if amount == None else amount
        reference = "PIXPAYMENT" if reference == None else reference

        self.cur.execute(f'INSERT INTO pixhos (id, name, city, key_type, key, amount, reference, payload) VALUES (null, "{name}", "{city}", "{key_type}", "{key}", "{amount}", "{reference}", "{payload}")')

        self.con.commit()

    def insert_config(self, prt_default: str, qrcode_size: int, qrcode_border: int):
        self.cur.execute(f'INSERT INTO config (prt_default, qrcode_size, qrcode_border) VALUES ("{prt_default}", {qrcode_size}, {qrcode_border})')
        self.con.commit()

    def __delete_by_id(self, table: str, id: int):
        self.cur.execute(f'DELETE FROM {table} WHERE id = {id}')
        self.con.commit()

    def delete_pixhos_by_id(self, id: int):
        self.__delete_by_id('pixhos', id)

    def update_config(self, prt_default: str, qrcode_size:int, qrcode_border: int):
        self.cur.execute(f'UPDATE config SET prt_default = "{prt_default}", qrcode_size={qrcode_size}, qrcode_border={qrcode_border}')
        self.con.commit()

    def __select_all(self, table: str, column: list = None):
        self.cur.execute(f'SELECT * FROM {table}')
        # print(list(map(lambda x: x[0], self.cur.description)))
        return self.cur.fetchall();

    def __select_one(self, table: str, column: list = None):
        self.cur.execute(f'SELECT * FROM {table}')
        return self.cur.fetchone()

    def __call__(self):
        print("Called!!")

    def __del__(self):
        self.con.close()