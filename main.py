def gen_crl(n:int,start_id:int,exp:str,rev:str)->list:
    """Каждый CRL поступает в OpenSSL как certindex(файл .csv разделитель tab)
    n:количество сертификатов, которые хотим отозвать,
    start_id:с какого серийного номера отзываем сертификаты
    exp:дата истечения срока действия сертификата
    rev:дата отзыва сертификата
    return:list, подавать на csv/pandas
    """
    lst=[]
    for i in range(n):
        cur_ser_num=start_id+i
        cur_ser_num=hex(cur_ser_num)[2:].zfill(40)
        info="/CN=subcert{}/ST=Some-State/C=AU/O=Internet Widgits Pty".format(cur_ser_num)
        cur_cert=["R",exp,rev,cur_ser_num,"unknown",info]
        lst.append(cur_cert)
    return lst

if __name__=="__main__":
    import datetime
    import csv
    time_now=datetime.datetime.now()+datetime.timedelta(days=60)
    time_1sec_later=time_now+datetime.timedelta(seconds=1)
    exp = time_now.strftime("%y%m%d%H%M%SZ")
    rev=time_1sec_later.strftime("%y%m%d%H%M%SZ")
    print(exp,rev)
    res_lst=gen_crl(2*10**6-10**5,10**48,exp=exp,rev=rev)
    with open("certindex","w",newline='') as fout:
        writer=csv.writer(fout,delimiter='\t')
        writer.writerows(res_lst)
    