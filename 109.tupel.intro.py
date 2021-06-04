# Tuples are immutable
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Methods
print(days.count("Monday"))
print(len(days))
print(days[:2])
# days[2] = "Tuesday" #error
print(days)
print(type(days))