from pathlib import Path

path = Path('guest_book.txt')

guest_names = []

message = ""

while True:
    prompt = "\nWelcome dear guest, please write your name in the book!"
    prompt += "\nWhen everyone is done signing, please write 'done'. "
    guest_name = input(prompt)
    if guest_name == 'done':
        for guest in guest_names:
            message += f"{guest} wrote in the guest book!\n"
        path.write_text(message)
        break
    else:
        print(f"Thank you for coming, {guest_name}!")
        guest_names.append(guest_name)