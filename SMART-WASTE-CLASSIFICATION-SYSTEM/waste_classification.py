# Smart Waste Classification System
# Beginner-friendly Python project (rule-based)

from datetime import datetime

# Dictionary: item -> category
waste_db = {
    "banana peel": "Biodegradable",
    "vegetable": "Biodegradable",
    "fruit": "Biodegradable",
    "leaves": "Biodegradable",
    "newspaper": "Recyclable",
    "paper": "Recyclable",
    "plastic bottle": "Recyclable",
    "glass": "Recyclable",
    "metal": "Recyclable",
    "chip packet": "Non-recyclable",
    "thermocol": "Non-recyclable",
    "diaper": "Non-recyclable",
}

# Dictionary: category -> bin colour
bin_colour = {
    "Biodegradable": "Green bin",
    "Recyclable": "Blue bin",
    "Non-recyclable": "Black bin",
}


def classify(item):
    """Return the waste category of an item."""
    item = item.lower().strip()

    for key in waste_db:
        if key in item:
            return waste_db[key]

    return "Unknown"


def show_result(category):
    if category == "Biodegradable":
        tip = "Use it for compost."
    elif category == "Recyclable":
        tip = "Clean it and recycle."
    elif category == "Non-recyclable":
        tip = "Dispose of it carefully."
    else:
        tip = "Item not in the list."

    print("Category :", category)

    if category != "Unknown":
        print("Bin      :", bin_colour[category])

    print("Tip      :", tip)


def save_history(item, category):
    now = str(datetime.now())[:16]

    with open("history.txt", "a") as f:
        f.write(now + " | " + item)
        f.write(" | " + category + "\n")


def main():
    print("=" * 38)
    print(" SMART WASTE CLASSIFICATION SYSTEM")
    print("=" * 38)

    count = 0

    while True:
        item = input("\nEnter item (or exit): ")

        if item.lower().strip() == "exit":
            break

        if item.strip() == "":
            print("Please type something.")
            continue

        category = classify(item)
        show_result(category)
        save_history(item, category)
        count += 1

    print("\nItems checked:", count)
    print("Thank you! Keep the city clean.")


main()