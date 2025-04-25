import random

dice = {
    1: "⚀", 2: "⚁", 3: "⚂",
    4: "⚃", 5: "⚄", 6: "⚅"
}

while input("Roll dice? (y/n): ").lower() == "y":
    print(dice[random.randint(1, 6)])
