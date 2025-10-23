"""
Program: Marital Status & Age Group Counter (While + Nested If/Elif)
Author: Donaven Bruce
Description: Asks for marital status and age of 6 people. Counts totals for
married/single/divorced/separated, and within each status counts ages in 20's,
30's, 40's, and >= 50. Prints required summaries. Shows error messages for
unknown marital status and for ages below 20.
"""

# totals and age-group counters per status
married_count = 0
married_over_50 = 0
married_40s = 0
married_30s = 0
married_20s = 0

single_count = 0
single_over_50 = 0
single_40s = 0
single_30s = 0
single_20s = 0

divorced_count = 0
divorced_over_50 = 0
divorced_40s = 0
divorced_30s = 0
divorced_20s = 0

separated_count = 0
separated_over_50 = 0
separated_40s = 0
separated_30s = 0
separated_20s = 0

# loop for 6 people
i = 0
while i < 6:
    status_raw = input("Please enter persons marital status: \n")
    age = int(input("Please enter persons age: \n"))
    status = status_raw.strip().lower()

    # nested if/elif by status, then age groups
    if status == "married":
        married_count = married_count + 1
        if age >= 50:
            married_over_50 = married_over_50 + 1
        elif 40 <= age < 50:
            married_40s = married_40s + 1
        elif 30 <= age < 40:
            married_30s = married_30s + 1
        elif 20 <= age < 30:
            married_20s = married_20s + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif status == "single":
        single_count = single_count + 1
        if age >= 50:
            single_over_50 = single_over_50 + 1
        elif 40 <= age < 50:
            single_40s = single_40s + 1
        elif 30 <= age < 40:
            single_30s = single_30s + 1
        elif 20 <= age < 30:
            single_20s = single_20s + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif status == "divorced":
        divorced_count = divorced_count + 1
        if age >= 50:
            divorced_over_50 = divorced_over_50 + 1
        elif 40 <= age < 50:
            divorced_40s = divorced_40s + 1
        elif 30 <= age < 40:
            divorced_30s = divorced_30s + 1
        elif 20 <= age < 30:
            divorced_20s = divorced_20s + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif status == "separated":
        separated_count = separated_count + 1
        if age >= 50:
            separated_over_50 = separated_over_50 + 1
        elif 40 <= age < 50:
            separated_40s = separated_40s + 1
        elif 30 <= age < 40:
            separated_30s = separated_30s + 1
        elif 20 <= age < 30:
            separated_20s = separated_20s + 1
        else:
            print("Sorry ! The person does not belong to any group")
    else:
        print("Sorry ! The marital status does not belong to one of the known statuses")

    i = i + 1

# summaries
print("*****")
print("The number of people who are married is: " + str(married_count))
print("The number of people who are married and over the 50 is: " + str(married_over_50))
print("The number of people who are married and in the age group of 40's is: " + str(married_40s))
print("The number of people who are married and in the age group of 30's is: " + str(married_30s))
print("The number of people who are married and in the age group of 20's is: " + str(married_20s))
print("*****")
print("The number of people who are single is: " + str(single_count))
print("The number of people who are single and over the 50 is: " + str(single_over_50))
print("The number of people who are single and in the age group of 40's is: " + str(single_40s))
print("The number of people who are single and in the age group of 30's is: " + str(single_30s))
print("The number of people who are single and in the age group of 20's is: " + str(single_20s))
print("*****")
print("The number of people who are divorced is: " + str(divorced_count))
print("The number of people who are divorced and over the 50 is: " + str(divorced_over_50))
print("The number of people who are divorced and in the age group of 40's is: " + str(divorced_40s))
print("The number of people who are divorced and in the age group of 30's is: " + str(divorced_30s))
print("The number of people who are divorced and in the age group of 20's is: " + str(divorced_20s))
print("*****")
print("The number of people who are separated is: " + str(separated_count))
print("The number of people who are separated and over the 50 is: " + str(separated_over_50))
print("The number of people who are separated and in the age group of 40's is: " + str(separated_40s))
print("The number of people who are separated and in the age group of 30's is: " + str(separated_30s))
print("The number of people who are separated and in the age group of 20's is: " + str(separated_20s))
print("*****")
