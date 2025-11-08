"""
Program: Region & Marital Status Counter (5 Users)
Author: Donaven Bruce
Description: Prompts for state and marital status of five users (case-insensitive),
counts users by region (Western, Eastern, Southern) and by marital status within
each region, then displays the formatted results. Prints messages for invalid
state or invalid marital status inputs during processing.
"""

# region counters
western_count = 0
western_married = 0
western_single = 0
western_divorced = 0
western_separated = 0

eastern_count = 0
eastern_married = 0
eastern_single = 0
eastern_divorced = 0
eastern_separated = 0

southern_count = 0
southern_married = 0
southern_single = 0
southern_divorced = 0
southern_separated = 0

# collect inputs 
state1 = input("Please enter the state where the first person resides :\n")
status1 = input("Please enter marital status of first person :\n")

state2 = input("Please enter the state where the second person resides :\n")
status2 = input("Please enter marital status of second person :\n")

state3 = input("Please enter the state where the third person resides :\n")
status3 = input("Please enter marital status of third person :\n")

state4 = input("Please enter the state where the fourth person resides :\n")
status4 = input("Please enter marital status of fourth person :\n")

state5 = input("Please enter the state where the fifth person resides :\n")
status5 = input("Please enter marital status of fifth person :\n")

# normalize first person's inputs and tally
state1_u = state1.upper()
status1_l = status1.lower()

if state1_u in ("CA", "NV", "AR", "WA"):
    western_count = western_count + 1
    if status1_l == "married":
        western_married = western_married + 1
    elif status1_l == "single":
        western_single = western_single + 1
    elif status1_l == "divorced":
        western_divorced = western_divorced + 1
    elif status1_l == "separated":
        western_separated = western_separated + 1
    else:
        print("The marital status is invalid")
elif state1_u in ("NY", "MA", "FL"):
    eastern_count = eastern_count + 1
    if status1_l == "married":
        eastern_married = eastern_married + 1
    elif status1_l == "single":
        eastern_single = eastern_single + 1
    elif status1_l == "divorced":
        eastern_divorced = eastern_divorced + 1
    elif status1_l == "separated":
        eastern_separated = eastern_separated + 1
    else:
        print("The marital status is invalid")
elif state1_u in ("TX", "AL", "GA"):
    southern_count = southern_count + 1
    if status1_l == "married":
        southern_married = southern_married + 1
    elif status1_l == "single":
        southern_single = southern_single + 1
    elif status1_l == "divorced":
        southern_divorced = southern_divorced + 1
    elif status1_l == "separated":
        southern_separated = southern_separated + 1
    else:
        print("The marital status is invalid")
else:
    print("Invalid state")

# second person
state2_u = state2.upper()
status2_l = status2.lower()

if state2_u in ("CA", "NV", "AR", "WA"):
    western_count = western_count + 1
    if status2_l == "married":
        western_married = western_married + 1
    elif status2_l == "single":
        western_single = western_single + 1
    elif status2_l == "divorced":
        western_divorced = western_divorced + 1
    elif status2_l == "separated":
        western_separated = western_separated + 1
    else:
        print("The marital status is invalid")
elif state2_u in ("NY", "MA", "FL"):
    eastern_count = eastern_count + 1
    if status2_l == "married":
        eastern_married = eastern_married + 1
    elif status2_l == "single":
        eastern_single = eastern_single + 1
    elif status2_l == "divorced":
        eastern_divorced = eastern_divorced + 1
    elif status2_l == "separated":
        eastern_separated = eastern_separated + 1
    else:
        print("The marital status is invalid")
elif state2_u in ("TX", "AL", "GA"):
    southern_count = southern_count + 1
    if status2_l == "married":
        southern_married = southern_married + 1
    elif status2_l == "single":
        southern_single = southern_single + 1
    elif status2_l == "divorced":
        southern_divorced = southern_divorced + 1
    elif status2_l == "separated":
        southern_separated = southern_separated + 1
    else:
        print("The marital status is invalid")
else:
    print("Invalid state")

# third person
state3_u = state3.upper()
status3_l = status3.lower()

if state3_u in ("CA", "NV", "AR", "WA"):
    western_count = western_count + 1
    if status3_l == "married":
        western_married = western_married + 1
    elif status3_l == "single":
        western_single = western_single + 1
    elif status3_l == "divorced":
        western_divorced = western_divorced + 1
    elif status3_l == "separated":
        western_separated = western_separated + 1
    else:
        print("The marital status is invalid")
elif state3_u in ("NY", "MA", "FL"):
    eastern_count = eastern_count + 1
    if status3_l == "married":
        eastern_married = eastern_married + 1
    elif status3_l == "single":
        eastern_single = eastern_single + 1
    elif status3_l == "divorced":
        eastern_divorced = eastern_divorced + 1
    elif status3_l == "separated":
        eastern_separated = eastern_separated + 1
    else:
        print("The marital status is invalid")
elif state3_u in ("TX", "AL", "GA"):
    southern_count = southern_count + 1
    if status3_l == "married":
        southern_married = southern_married + 1
    elif status3_l == "single":
        southern_single = southern_single + 1
    elif status3_l == "divorced":
        southern_divorced = southern_divorced + 1
    elif status3_l == "separated":
        southern_separated = southern_separated + 1
    else:
        print("The marital status is invalid")
else:
    print("Invalid state")

# fourth person
state4_u = state4.upper()
status4_l = status4.lower()

if state4_u in ("CA", "NV", "AR", "WA"):
    western_count = western_count + 1
    if status4_l == "married":
        western_married = western_married + 1
    elif status4_l == "single":
        western_single = western_single + 1
    elif status4_l == "divorced":
        western_divorced = western_divorced + 1
    elif status4_l == "separated":
        western_separated = western_separated + 1
    else:
        print("The marital status is invalid")
elif state4_u in ("NY", "MA", "FL"):
    eastern_count = eastern_count + 1
    if status4_l == "married":
        eastern_married = eastern_married + 1
    elif status4_l == "single":
        eastern_single = eastern_single + 1
    elif status4_l == "divorced":
        eastern_divorced = eastern_divorced + 1
    elif status4_l == "separated":
        eastern_separated = eastern_separated + 1
    else:
        print("The marital status is invalid")
elif state4_u in ("TX", "AL", "GA"):
    southern_count = southern_count + 1
    if status4_l == "married":
        southern_married = southern_married + 1
    elif status4_l == "single":
        southern_single = southern_single + 1
    elif status4_l == "divorced":
        southern_divorced = southern_divorced + 1
    elif status4_l == "separated":
        southern_separated = southern_separated + 1
    else:
        print("The marital status is invalid")
else:
    print("Invalid state")

# fifth person
state5_u = state5.upper()
status5_l = status5.lower()

if state5_u in ("CA", "NV", "AR", "WA"):
    western_count = western_count + 1
    if status5_l == "married":
        western_married = western_married + 1
    elif status5_l == "single":
        western_single = western_single + 1
    elif status5_l == "divorced":
        western_divorced = western_divorced + 1
    elif status5_l == "separated":
        western_separated = western_separated + 1
    else:
        print("The marital status is invalid")
elif state5_u in ("NY", "MA", "FL"):
    eastern_count = eastern_count + 1
    if status5_l == "married":
        eastern_married = eastern_married + 1
    elif status5_l == "single":
        eastern_single = eastern_single + 1
    elif status5_l == "divorced":
        eastern_divorced = eastern_divorced + 1
    elif status5_l == "separated":
        eastern_separated = eastern_separated + 1
    else:
        print("The marital status is invalid")
elif state5_u in ("TX", "AL", "GA"):
    southern_count = southern_count + 1
    if status5_l == "married":
        southern_married = southern_married + 1
    elif status5_l == "single":
        southern_single = southern_single + 1
    elif status5_l == "divorced":
        southern_divorced = southern_divorced + 1
    elif status5_l == "separated":
        southern_separated = southern_separated + 1
    else:
        print("The marital status is invalid")
else:
    print("Invalid state")

# final output blocks 
print("*****")
print("The number of people who belong to Western region is :" + str(western_count))
print("The number of people who are married in Western region is :" + str(western_married))
print("The number of people who are single in Western region is :" + str(western_single))
print("The number of people who are divorced in Western region is :" + str(western_divorced))
print("The number of people who are separated in Western region is :" + str(western_separated))
print("*****")
print("The number of people who belong to Eastern region is :" + str(eastern_count))
print("The number of people who are married in Eastern region is :" + str(eastern_married))
print("The number of people who are single in Eastern region is :" + str(eastern_single))
print("The number of people who are divorced in Eastern region is :" + str(eastern_divorced))
print("The number of people who are separated in Eastern region is :" + str(eastern_separated))
print("*****")
print("The number of people who belong to Soutern region is:" + str(southern_count))
print("The number of people who are married in Soutern region is :" + str(southern_married))
print("The number of people who are single in Soutern region is :" + str(southern_single))
print("The number of people who are divorced in Soutern region is :" + str(southern_divorced))
print("The number of people who are separated in Soutern region is :" + str(southern_separated))
print("*****")
