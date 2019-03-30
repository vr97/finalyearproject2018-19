import twitter
import xlwt
import time
from datetime import datetime

now = datetime.now()
api = twitter.Api(consumer_key='ZkueGAecI0y6rrbwbPrN3KcRg',

                 consumer_secret='VN5O8rcKYmCF6SSFNZtU3QkxH1l47vrU4I3uaWc6Cdnub2XhIB',
                 access_token_key='1046326010713714688-JNIZx8CXJbErXnRaEiblSF1mctEKP8',
                 access_token_secret='BGgxzDGQpoHhEWFN13HpPqrpPO24GPmuFtb16an7OYoCk')

def getData(search_string): #function to fetch tweet texts
    try:
        tweets_fetched=api.GetSearch(search_string,count=50,lang='en')
        print("Great! We fetched " +str(len(tweets_fetched))+" tweets with the term "+search_string+"!!")
        return [status.text for status in tweets_fetched]
    except:
        print ("Sorry there was an error!")
    return None


wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet 1')
primary_key = 1
row = 0
# for loop for running the statements after every 2 minutes.
while True:
    print("Timer restarted")
    # calling the api
    result = getData("RahulGandhi pulwama")
    # saving the data in xcel sheetoff
    hour = now.hour
    day = now.day
    minutes = now.minute
    for tweet in result:
        sheet1.write(row,0,primary_key)
        sheet1.write(row,1,tweet)
        sheet1.write(row,2,day)
        sheet1.write(row,3,hour)
        sheet1.write(row,4,minutes)
        row += 1
        primary_key += 1
    wb.save('narendra modi.xls')
    time.sleep(900) # 30 minutes
    api = twitter.Api(consumer_key='ZkueGAecI0y6rrbwbPrN3KcRg',

                      consumer_secret='VN5O8rcKYmCF6SSFNZtU3QkxH1l47vrU4I3uaWc6Cdnub2XhIB',
                      access_token_key='1046326010713714688-JNIZx8CXJbErXnRaEiblSF1mctEKP8',
                      access_token_secret='BGgxzDGQpoHhEWFN13HpPqrpPO24GPmuFtb16an7OYoCk')


