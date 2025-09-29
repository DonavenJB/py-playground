#Donaven Bruce
#Program 3: My program prompts user for name of the movie, the number of adult and child tickets sold
#           Next I calculate gross revenue, amount paid to distributor, net revenue, 
#              Finally I print the output to the user

LABEL_W = 22
VALUE_W = 5

POS_PREFIX = "  $"   
NEG_PREFIX = "- $"  

ticket_price_adult = 6.00
ticket_price_child = 3.00
distributor_rate = .80

adult_ticket_sold = 0
child_ticket_sold = 0

movie_name = input("Enter the name of the movie: ")
adult_ticket_sold = float(input("Enter the number of adult tickets sold: "))
child_ticket_sold = float(input("Enter the number of child tikets sold: "))


gross_revenue = (adult_ticket_sold * ticket_price_adult) + (child_ticket_sold * ticket_price_child)

#Gross revenue times the rate charged by distributor give us the amount paid to distributor
distributor_cost = gross_revenue * distributor_rate

#The theater keeps only net revenue
net_revenue = gross_revenue - distributor_cost

print(f"{'Movie Name:':<{LABEL_W}}\"{movie_name}\"")
print(f"{'Adult tickets sold:':<{LABEL_W}}{adult_ticket_sold:>{VALUE_W}.0f}")
print(f"{'Child tickets sold:':<{LABEL_W}}{child_ticket_sold:>{VALUE_W}.0f}")
print(f"{'Gross revenue:':<{LABEL_W}}{POS_PREFIX}{gross_revenue:>{VALUE_W},.2f}")
print(f"{'Distributor:':<{LABEL_W}}{NEG_PREFIX}{distributor_cost:>{VALUE_W},.2f}")
print(f"{'Net revenue:':<{LABEL_W}}{POS_PREFIX}{net_revenue:>{VALUE_W},.2f}")
