import shelve
db = shelve.open('C:\\Users\\NOME\\Desktop\\Tkinter\\arquivosdb\\login\\login.db')
db['User'] = []
db['Pass'] = []