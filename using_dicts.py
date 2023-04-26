state_capitals = {"Washington": "Olymipa",
                  "Oregon": "Salem", "California": "Sacramento"}
# print(len(state_capitals))

# print(state_capitals["Washington"])

state_capitals["Washington"] = "Aberdeen"
state_capitals["Minnesota"] = "St Paul"
print(state_capitals)
del state_capitals["California"]
print(state_capitals)
removed_capital = state_capitals.pop("Oregon")
print(state_capitals)
print(removed_capital)
