import random
from faker import Faker

def generate_order_info():
    first_names = ["Маша", "Даша"]
    last_names = ["Петрова", "Иванова"]
    metro = ["Черкизовская", "Сокольники"]
    rental_periods = ['сутки', 'двое суток']
    scooter_colors = ['чёрный жемчуг', 'серая безысходность']

    fake = Faker()

    order_info = {
        'first_name': random.choice(first_names),
        'last_name': random.choice(last_names),
        'metro': random.choice(metro),
        'phone': fake.phone_number(),
        'address': f"{random.choice(['Московская', 'Ульяновых'])}, {random.randint(1, 999)}",
        'date': fake.date_between(start_date='-30d', end_date='+30d'),
        'rental_period': random.choice(rental_periods),
        'scooter_color': random.choice(scooter_colors),
        'comment': fake.text(max_nb_chars=200)
    }

    return order_info


