import pickle

def is_birthday_in_pi(birthday: str, pi_digits: str) -> bool:
    return birthday in pi_digits

# π raqamlarini o'qish va saqlash
with open('pi_million_digits.txt', 'r') as file:
    pi_digits = file.read().replace('\n', '')

with open('pi_digits.pkl', 'wb') as file:
    pickle.dump(pi_digits, file)

# Foydalanuvchidan ma'lumotlarni qabul qilish
def append_data_to_file(filename: str):
    with open(filename, 'a') as file:
        while True:
            user_input = input("Ma'lumot kiriting (to'xtatish uchun 'exit' yozing): ")
            if user_input.lower() == 'exit':
                break
            file.write(user_input + '\n')

append_data_to_file('user_data.txt')

# Tug'ilgan kunni tekshirish
with open('pi_digits.pkl', 'rb') as file:
    pi_digits = pickle.load(file)

birthday = input("Tug'ilgan kuningizni YYYYMMDD formatida kiriting: ")
if is_birthday_in_pi(birthday, pi_digits):
    print("Sizning tug'ilgan kuningiz π soni tarkibida mavjud!")
else:
    print("Sizning tug'ilgan kuningiz π soni tarkibida mavjud emas.")
