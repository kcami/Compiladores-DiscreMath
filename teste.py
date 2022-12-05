people: any = [[]]
bike: any = [[]]
cross: any = [[]]
people = [["Lindsay", 16, "female"], ["Tom", 21, "male"], ["Eric", 33, "male"], ["Marco", 13, "male"], ["Kristopher", 45, "male"], ["Kelly", 21, "female"], ["Mitchell", 24, "male"], ["Tammy", 30, "female"], ["Brad", 18, "male "]]
bike = [["Lindsay", "orange"], ["Tom", "black"], ["Eric", "green"], ["Marco", "orange"], ["Kristopher", "grey"], ["Kelly", "blue"], ["Mitchell", "red"], ["Tammy", "yellow"], ["Brad", "pink"]]
cross = [(a, b) for a in people for b in bike]
print(cross, end="")