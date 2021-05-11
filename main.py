#importing required modules
from covid import Covid
from covid_india import states
import win10toast as w
import time
#code starts here
print("============== Covinfo ================")
print("Loding.....")
cv = Covid()
covid = Covid(source="worldometers")
act = cv.get_total_active_cases()
rec = cv.get_total_recovered()
death = cv.get_total_deaths()
con = cv.get_total_confirmed_cases()
#notification system code starts here
def notify():
	toast.show_toast('Covinfo',f'Active cases: "{act}"\nConfirmed cases: "{con}"\nRecovered cases: "{rec}"\nDeceased: "{death}',icon_path="notificationicon.ico",duration=5)
toast = w.ToastNotifier()
notify()
#notification code ends here 
#main code starts here
def main():
	while(True):
		print("1.Global Count\n2.Active cases\n3.Confirmed cases\n4.Recovered cases")
		print("5.Deceased\n6.Get Covid update by country name\n7.Get covid update by state name(india)\n0.EXIT")
		choice = int(input("Enter number of your choice: "))

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
		elif choice==6:
			str=i=input("enter country name: ")
			cname = cv.get_status_by_country_name(i)
			print(cname)
		elif choice==7:
			str =s=input("enter state name: ")
			sdata = states.getdata(s)
			print(sdata)
		elif choice==0:
			print("Thank you for beeing here")
			break
		else:
			print("invalid option")
			main()
#main code ends here
main()
#end of the code
