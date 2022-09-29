quotes = open("/Users/alexjshepler/Desktop/Epoch Industry/Programs/Auto Post/new.txt", 'r+')

lines = quotes.readlines()
quotes.seek(0)
quotes.truncate()

lines = filter(lambda line: len(line) <= 280, lines)
quotes.writelines(lines)
