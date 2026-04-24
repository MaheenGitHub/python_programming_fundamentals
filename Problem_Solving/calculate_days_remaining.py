"""
how many days, weeks , months we have left if we live until 90 years old
input :
ur current age
output :
you have a days, b weeks and c months left

1 year -> 365 days -> 52 weeks -> 12 months

"""

current_age = input("Enter ur current age: "
)
remaining_age = 90 - int(current_age)
print(f"u have {remaining_age*365} days , {remaining_age*52} weeks and {remaining_age*12} months left")