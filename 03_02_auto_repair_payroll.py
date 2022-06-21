# This program named constants to represent the base hours and the overtime multiplier.

#Get work hours
hours = float(input("What is your work hours?: "))
#Set up the base hour and overtime multiplier 
base_hours = 40 #Base hours per week
ot_multiplier=1.5 #Over time multiplier
payrate = 10

if hours >base_hours:
    overtime_hours = hours - base_hours
    overtime_pay =overtime_hours*payrate *ot_multiplier
    gross_pay= base_hours* payrate+ overtime_pay 

else:
    gross_pay=hours*payrate



#Calculate and display the gross pay 

##if the work hours are greater than base hours
    #if hours >= base_hours:
##Calculate the gross pay with over time 
    #gross_pay =base_hours*payrate + payrate * ot_multiplier*(hours- base_hours)

##if the work hours are less than base hours
        #else:
##Calculate the gross pay
    #gross_pay =hours*payrate
##Display the gross pay    
print("your gross pay is", gross_pay, "RMB")


