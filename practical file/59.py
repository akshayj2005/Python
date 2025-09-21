# WAP in Python to determine Season based on month

def get_season(month):
    if month in [2, 3]:              # Vasant – Spring
        return "Vasant – Spring"
    elif month in [4, 5]:            # Grishma – Summer
        return "Grishma – Summer"
    elif month in [6, 7]:            # Varsha – Monsoon
        return "Varsha – Monsoon"
    elif month in [8, 9]:            # Sharad – Autumn
        return "Sharad – Autumn"
    elif month in [10, 11]:          # Hemant – Pre-winter
        return "Hemant – Pre-winter"
    elif month in [12, 1]:           # Shishir – Winter
        return "Shishir – Winter"
    else:
        return "Invalid month number!"

# Input from user
month = int(input("Enter month number (1-12): "))
print("Season:", get_season(month))

