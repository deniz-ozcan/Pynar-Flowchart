futbolPlayers = {
    '1': {
        'name': 'Cristiano Ronaldo dos Santos Aveiro',
        'yearOfBirth': '1985',
        "nationality": "Portugal",
        "current_team": "Manchester United",
        "history": "juventus, Real Madrid"
    },
    '2': {
        "name": 'Lionel Andrés Messi Cuccittini',
        'yearOfBirth': '1987',
        "nationality": "Argentina",
        "current_team": "Paris Saint Germain",
        "history": "Barcelona"
    },
    '3': {
        'name': 'Neymar da Silva Santos Junior',
        'yearOfBirth': '1992',
        "nationality": "brasil",
        "current_team": "Paris Saint Germain",
        "history": "Barcelona"
    }
}

id = input("Id of the player: ")
futbolPlayers = futbolPlayers.get(id)
print(f'Name of the player: {futbolPlayers.get("name")} ')
print(f'Nationality of the player: {futbolPlayers.get("nationality")} ')
print(f'Year of birth of the player: {futbolPlayers.get("yearOfBirth")} ')
print(f'Current team of the player: {futbolPlayers.get("current_team")} ')
print(f'History of the player: {futbolPlayers.get("history")} ')
print(" ")
id = input("What is the id of the player that you want to delete?: ")
futbolPlayers.pop(id)
print(futbolPlayers)
id = input("Id of the player: ")
name = input("Name of the player: ")
nationality = input("Nationality of the player: ")
yearOfBirth = input("Year of birth of the player: ")
current_team = input("Current team of the player: ")
history = input("History of the player: ")

futbolPlayers.update({
    id: {
        'name': name,
        'yearOfBirth': yearOfBirth,
        "nationality": nationality,
        "current_team": current_team,
        "history": history.split(",")
    }

})
print(futbolPlayers)