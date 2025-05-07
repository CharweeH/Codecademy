#create empty list

gamers = []

#create funtion that will update empty list

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Information is missing")

#add first gamer

kimberly = {"name": "Kimberly", "availability": ["Monday", "Thursday", "Sunday"]}

add_gamer(kimberly, gamers)

#print(gamers)

#add more gamers

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#finding the perfect availability

def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer.get("availability", []):
            available_frequency[day] += 1

#best night to run Abruptly Goblins

calculate_availability(gamers, count_availability)

#print(count_availability)

#day with most available gamers

def find_best_night(availability_table):
    return max(availability_table, key=availability_table.get)

game_night = find_best_night(count_availability)

print(game_night)

def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer.get("availability", [])]

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

#generating email to send to participants

form_email = """

Dear {name},

{game} will be played on {day}! Come join us at the Sorcery Society!

Best wishes

Sorcery Society"""

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer["name"], day=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")

#sending email to participants who couldn't attend

unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer.get("availability")]

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)

#print(second_night)

#second night email

available_sencond_game_night = available_on_night(gamers, second_night)

send_email(available_sencond_game_night, second_night, "Abruptly Goblins")