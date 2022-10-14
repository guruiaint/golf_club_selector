# Stock club distances
yardage_to_club = {
    "275" : "D",
    "235" : "3w",
    "210" : "5w",
    "194" : "4i",
    "181" : "5i",
    "169" : "6i",
    "157" : "7i",
    "145" : "8i",
    "133" : "9i",
    "121" : "Pw",
    "107" : "Aw",
    "95" : "Sw",
    "81" : "Lw",
}
while True:
    # Input Check
    def get_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                break
            except ValueError:
                print("Sorry, please enter positive or negative numbers only")
                continue
        return value

    # Variable inputs
    yards = get_float("Type distance in yards then press Enter:")

    slope = get_float("Type slope in feet then press Enter (positive for uphill hole location, negative for downhill hole location):")

    wind = get_float("Type wind in mph then press Enter (positive for headwind, negative for tailwind, 0 for crosswind):")

    def yardage_corrector(yards, slope, wind, yardage_to_club):
        # Equation for slope variable
        s_distance = slope / 3 + yards

        new_yardage = s_distance
        if wind >= 0:
    # Equation for wind variable
        # Headwind add 1% of yards per mph (c. yardage = wind value as percent * yards)
            c_distance = (wind * .01 + 1) * new_yardage
        elif wind < 0:
        # Tailwind subtract 0.5% of yards per mph (c. yardage = wind value as percent * yards)
            c_distance = ((wind * .005) + 1) * new_yardage

        res = yardage_to_club[min(yardage_to_club.keys(), key = lambda key: abs(float(key) - c_distance))]
        print("Corrected Yardage:", round(c_distance), "yards", "Use:", (res))

    yardage_corrector(yards, slope, wind, yardage_to_club)

    new_yardage = input("Would you like to check a new yardage? Type Y (uppercase) for yes or any other key for no, then press Enter:")
    if new_yardage.upper() == "Y":
        continue
    print("Goodbye...")
    break

