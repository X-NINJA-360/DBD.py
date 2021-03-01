from dbd_py import dbot
test=dbot({
    "prefix":"!",
    "token":"твой токен"
})

test.command({
    "name":"имя команды после префикса",
    "code":["код", "код", "код", "и т.д."]
})

test.start()
