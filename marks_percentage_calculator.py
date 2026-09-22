print("Marks Percentage Calculator")

name = input()

sub1 = float(input())
sub2 = float(input())
sub3 = float(input())
sub4 = float(input())
sub5 = float(input())

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("\n---Student Marks---")
print("Name:",name)
print("Total marks:",total)
print("Percentage:",percentage, "%")