import prettytable
table = prettytable.PrettyTable()
# from prettytable import PrettyTable()
# table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "scatterbug", "Pigedot"])
table.add_column("Pokemon Name", ["Electro","Bug","Flying"])
table.align["Pokemon Name"] = "l"
table.align["Pokemon Name"] = "r"
print(table)