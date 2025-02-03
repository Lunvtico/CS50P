Hello = input("Select your greeting: ").strip().lower()

if "hello" in Hello:
  print("You receive $0")

elif Hello.startswith("h"):
  print("You receive $20")

else:
 print("You receive $100")
