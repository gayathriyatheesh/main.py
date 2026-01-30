sid = input()
email = input()
password = input()
ref = input()

valid = True

if sid[0:3] != "CSE":
    valid = False
if len(sid) != 7:
    valid = False
if sid[3] != "-":
    valid = False
if not sid[4:7].isdigit():
    valid = False

if "@" not in email or "." not in email:
    valid = False
if email[0] == "@" or email[-1] == "@":
    valid = False
if email[-4:] != ".edu":
    valid = False

if len(password) < 8:
    valid = False
if not password[0].isupper():
    valid = False
if not ("0" in password or "1" in password or "2" in password or "3" in password or
        "4" in password or "5" in password or "6" in password or "7" in password or
        "8" in password or "9" in password):
    valid = False

if ref[0:3] != "REF":
    valid = False
if len(ref) != 6:
    valid = False
if not ref[3:5].isdigit():
    valid = False
if ref[-1] != "@":
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")
