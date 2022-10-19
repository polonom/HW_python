def log_in(linenn:str):
    f=open('dat.csv','a',newline='')
    f.write(f'{linenn}')
    f.close