#importing required modules
from covid import Covid
from covid_india import states
import win10toast as w
import time
from bs4 import BeautifulSoup
import requests
#code starts here
print("============== Covinfo ================")
print("Loding.....")
cv = Covid()
covid = Covid(source="worldometers")     #source for data in covid module
act = cv.get_total_active_cases()
rec = cv.get_total_recovered()
death = cv.get_total_deaths()
con = cv.get_total_confirmed_cases()
india = cv.get_status_by_country_name('India')
#vaccination data code
req  = requests.get('https://www.mohfw.gov.in/')
bs = BeautifulSoup(req.text,'html.parser')
vaccin_data = bs.find("div",class_ = "fullbol")
tested = bs.find("span",class_="tested")
#notification system code starts here
def notify():
	toast.show_toast('Covinfo',f'Golbal Count\nActive cases: "{act}"\nRecovered cases: "{rec}"\nDeceased: "{death}"',icon_path="notificationicon.ico",duration=5)
toast = w.ToastNotifier()
notify()
#notification code ends here 
def main():
	while(True):
		print("1.Global Count\n2.Active cases\n3.Confirmed cases\n4.Recovered cases")
		print("5.Deceased\n6.India count\n7.Get Covid update by country name")
		print("8.Get covid update by state name(india)\n9.vaccination_data(india)\n10.Total no tested case in 24hours\n0.Exit")
		choice = int(input("Enter number of your choice: "))
		print("-----------------------------------")
		if choice==1:
			print("Active cases: ",act,"\nConfirmed cases: ",con,"\nRecovered cases: ",rec,"\nDeceased: ",death)
		elif choice==2:
			print("Active cases: ",act)
		elif choice==3:
			print("Confirmed cases: ",con)
		elif choice==4:
			print("Recovered cases: ",rec)
		elif choice==5:
			print("Deceased: ",death)
		elif choice == 6:
			print(f"India Covid Count: {india}")
		elif choice==7:
			str=i=input("enter country name: ")
			cname = cv.get_status_by_country_name(i)
			print(cname)
		elif choice==8:
			str =s=input("enter state name: ")
			sdata = states.getdata(s)
			print(sdata)
		elif choice==9:
			raw = (vaccin_data.text.split())
			print(raw[0]+" "+raw[1]+' Done'+raw[2]+' '+raw[3])
		elif choice == 10:
			print(tested.text)
		elif choice==0:
			print("Thank you for beeing here")
			break
		else:
			print("invalid option")
			main()
		print("-----------------------------------")
main()
#end of the code
