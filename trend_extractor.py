import csv
import traceback
import datetime

def getInBetweenDates(start_date,end_date):
   date_list = [start_date]
   try:
     sdate = datetime.datetime.strptime(start_date,'%Y-%m-%d')
     edate = datetime.datetime.strptime(end_date,'%Y-%m-%d')

     new_date = sdate + datetime.timedelta(days=1)
   
     while new_date < edate:
        new_time = datetime.datetime.strftime(new_date,'%Y-%m-%d')
        date_list.append(new_time)
        new_date = new_date + datetime.timedelta(days=1)

     date_list.append(end_date)

   except:
      traceback.print_exc()

   return date_list
      

def convert2Daily(csv_file,outfile):
   try:
      fin = open(csv_file,'r')
      finreader = csv.reader(fin,delimiter=',')

      fout = open(outfile,'w')

      count = 0
      for line in finreader:
         if count > 0:
            wdate = line[0].split(' ')
            start_date = wdate[0]
            end_date   = wdate[2]
            gtrend     = line[1]

            date_list = getInBetweenDates(start_date,end_date)

            for item in date_list:
               dlist = [item,str(gtrend)]
 
               fout.write("%s\n"%','.join(dlist))
       
         count += 1

      fin.close()
      fout.close()

   except:
      traceback.print_exc()

convert2Daily('/Users/nehachoudhary/Google_Trends.csv','/tmp/Daily_GTrend.csv')
