n=["a","e","i","o","u"]
s=input()
if s.isdigit():
	print("invalid")
elif s in n:
	print("Vowels")
else:
	print("Consonant")
