import shelve
db = shelve.open('C:\\Users\\wellington\\Desktop\\Tkinter\\arquivosdb\\login\\login.db')
db['User'] = []
db['Pass'] = []