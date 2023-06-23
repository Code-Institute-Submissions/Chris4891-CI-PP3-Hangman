import random
import math

def load_words_from_txt_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words

def start_game():
    username = username_entry.get()
    if username:
        username_label.pack_forget()
        username_entry.pack_forget()
        start_button.pack_forget()

        initialize_game()
        window.title(f"Hangman Game - {username}")
        hangman_label.pack()
        word_label.pack()
        guess_label.pack()
        guess_entry.pack()
        guess_button.pack()
        message_label.pack()
    else:
        message_label.config(text="Please enter your name.")

def initialize_game():
    global guess_word, remaining_attempts, guessed_letters

    guess_word = random.choice(words)
    remaining_attempts = 6
    guessed_letters = set()

    update_word_display()
    update_image()

def update_word_display():
    masked_word = ' '.join([letter if letter in guessed_letters else '_' for letter in guess_word])
    word_label.config(text=masked_word)

def update_image():
    image_path = f'img/hangman{6 - remaining_attempts}.png'
    hangman_image.config(file=image_path)

def process_guess():
    global remaining_attempts

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            message_label.config(text="You've already guessed that letter.")
        elif guess in guess_word:
            guessed_letters.add(guess)
            update_word_display()

            if all(letter in guessed_letters for letter in guess_word):
                message_label.config(text="Congratulations! You guessed the word!")
        else:
            remaining_attempts -= 1
            update_image()

            if remaining_attempts == 0:
                end_game()
    else:
        message_label.config(text="Please enter a single letter.")

def end_game():
    window.withdraw()

    game_over_window = tk.Toplevel()
    game_over_window.title("Game Over")
    game_over_window.configure(bg="red")

    game_over_frame = tk.Frame(game_over_window, bg="red")
    game_over_frame.pack(pady=20)

    game_over_label = tk.Label(game_over_frame, text="Game Over", font=('Arial', 24), bg="red", fg="white")
    game_over_label.pack(pady=20)

    restart_button = tk.Button(game_over_frame, text="Restart Game", command=restart_game, font=('Arial', 16), bg="white")
    restart_button.pack(pady=20)

    game_over_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    game_over_window.mainloop()

def restart_game():
    initialize_game()
    window.deiconify()

    # Clear previous game state
    guess_entry.delete(0, tk.END)
    message_label.config(text="")


