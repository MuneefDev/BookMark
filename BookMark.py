# ------------------------------------------------------
# -- BookMark Program
# -- Date 25 of may 2021
# -- program will ask user to input
# -- his favorite websits and will make a BookMark
# ------------------------------------------------------


print("*" * 60)
print(" Welcome to BookMark program owned by @iiMuneef ".center(60, "*"))
print("*" * 60)

MyFavoritWebs = []
MaximumWebs = 5

while MaximumWebs > 0:
    Web = input(
        "Enter Websit to add in your BookMark without https:// ").strip().lower()
    MyFavoritWebs.append(f"https://{Web}")
    MaximumWebs -= 1
    print(MyFavoritWebs)
    print(f"Websit has been added, {MaximumWebs} places left! ")

else:
    print("BookMark is Full, can't add more Websites. ")

# cheak if list is not empty and print all websits to user
if len(MyFavoritWebs) > 0:
    MyFavoritWebs.sort()
    print("=" * 60)
    index = 0
    print("printing the list of your BookMark ... ")
    while len(MyFavoritWebs) > index:
        print(MyFavoritWebs[index])
        index += 1
        
