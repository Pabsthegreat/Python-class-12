with open ('fileNames.txt') as f:
    st = ' '
    while st:
        if st != '':
            name = f.readline()
            name = name.replace('\n','')
            if name != '':
                with open (name) as file:
                    co_dig = 0
                    co_lin = 0
                    co_wor = 0
                    con = ' '
                    while con:
                        if st != '':
                            con = file.readline()
                            con = con.split()
                            for i in con:
                                if i.isdigit():
                                    co_dig += len(i)
                                if i.isalpha():
                                    co_wor +=1
                        co_lin +=1
                print(name)
                print(co_dig, 'digits in the file')
                print(co_lin, 'lines in the file')
                print(co_wor, 'words in the file')
        
        else:
            break
                            
