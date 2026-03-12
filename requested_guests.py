requested_guests = ['irina']

if requested_guests:
    for guest in requested_guests:
        print(f"Hello, {guest.title()}!")
else:
    print('В списке пока никого нет')