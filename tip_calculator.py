def calculate():
    while True:
        bill = input("How much was the bill? ")
        try:
            bill = float(bill)
        except:
            print("Invalid value.")
            continue
        break

    levels = {
        'good': 20.,
        'fair': 15.,
        'bad': 10.
    }

    while True:
        service_quality = input("How was the service: good, bad, or fair? ")
        if service_quality in levels:
            break
        else:
            print("Invalid input.")
            continue

    while True:
        party_size = input("How many people are splitting the bill? ")
        try:
            party_size = float(party_size)
        except:
            print("Invalid value.")
            continue
        break

    tip = bill * (levels[service_quality] / 100)
    total = bill + tip

    print("Tip amount: $%.2f" % tip)
    print ("Total amount: $%.2f" % total)
    print("Amount per person: $%.2f" % (total / party_size))