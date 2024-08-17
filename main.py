from tkinter import messagebox, simpledialog, Label, Tk

root = Tk()
root.title("Secret Message")
root.configure(background="#20211A")
root.geometry("500x500")

# get task
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

# get message
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

# get even letters
def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

# get odd letters
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

# encrypt or decrypt message
def swap_letters(message):
    letter_list = []
    # ensure message is even
    if not is_even(len(message)):
        message = message + 'x'
    # fetch even letters from message
    even_letters = get_even_letters(message)
    # fetch odd letters from message 
    odd_letters = get_odd_letters(message)
    # swap even(i) with odd(i)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    # convert list to string
    new_message = ''.join(letter_list)
    return new_message

# remove last element
def remove_last_letter(message):
    letter_list = list(message)
    letter_list.pop()
    return ''.join(letter_list)

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Cipher text of the secret message is: ', encrypted)
    elif task == 'decrypt':
        message = get_message()
        if is_even(len(message)):
            decrypted = swap_letters(message)
            messagebox.showinfo('Plain text of the secret message is: ', decrypted)
        else:
            plaintext = swap_letters(message)
            decrypted = remove_last_letter(plaintext)
            messagebox.showinfo('Plain text of the secret message is: ', decrypted)
    else:
        break

root.mainloop()