
ip = input("Enter an IP address: ")

parts = ip.split(".")

print("\n=== IP Security Report ===")

# Check IP format

if len(parts) != 4:
  print("Invalid IP Address Format")

else:

  valid = True

for part in parts:
    if not part.isdigit():
        valid = False
        break

    number = int(part)

    if number < 0 or number > 255:
        valid = False
        break

if valid:

    if ip == "0.0.0.0":
        print("Type: Unspecified Address")
        print("Risk Level: High")
        print("Suspicious or invalid address detected.")

    elif ip.startswith("127."):
        print("Type: Loopback Address")
        print("Risk Level: Low")
        print("Used by the local machine.")

    elif (ip.startswith("192.168.")
    or ip.startswith("10.")
    or (parts[0] == "172" and 16 <= int(parts[1]) <= 31)):
        print("Type: Private IP Address")
        print("Risk Level: Low")
        print("Used inside local networks.")

    else:
        print("Type: Public IP Address")
        print("Risk Level: Medium")
        print("Further investigation may be required.")

else:
    print("Invalid IP Address")

