import shelve
db = shelve.open('C:\\Users\\danil\\Desktop\\Tkinter\\arquivosdb\\login\\login.db')
db['User'] = []
db['Pass'] = []
