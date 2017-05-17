def ejec()
    for line in open('bd.sql'):
        c.execute(line)