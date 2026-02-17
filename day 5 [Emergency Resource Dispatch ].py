
requests = [10, 25, 60, -3, 0, 45, 80]


low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

total_valid = 0
removed_due_to_pli = 0


full_name = str(input("enter your name :"))


L = 0
for ch in full_name:
    if ch != " ":
        L = L + 1

PLI = L % 3


for value in requests:

    if value < 0:
        invalid_requests = invalid_requests + [value]

    elif value == 0:
        pass

    elif value >= 1 and value <= 20:
        low_demand = low_demand + [value]
        total_valid = total_valid + 1

    elif value >= 21 and value <= 50:
        moderate_demand = moderate_demand + [value]
        total_valid = total_valid + 1

    else:
        high_demand = high_demand + [value]
        total_valid = total_valid + 1




if PLI == 0:
    removed_due_to_pli = len(low_demand)
    low_demand = []

elif PLI == 1:
    removed_due_to_pli = len(high_demand)
    high_demand = []

else:
    removed_due_to_pli = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []



print("Full Name Length (L):", L)
print("PLI Value:", PLI)

if PLI == 0:
    print("Applied Rule: Rule A (Removed Low Demand)")
elif PLI == 1:
    print("Applied Rule: Rule B (Removed High Demand)")
else:
    print("Applied Rule: Rule C (Only Moderate Demand Kept)")

print("\nTotal Valid Requests:", total_valid)
print("Removed Due To PLI:", removed_due_to_pli)

print("\nLow Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
