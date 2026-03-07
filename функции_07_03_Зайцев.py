tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}
def table(table_n,name,vip=False):
    tables[table_n] = [name, vip]
table(2, 'aaa', False)
table(3, 'bbb')
print(tables)
