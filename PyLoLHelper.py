import json
import urllib.request

with urllib.request.urlopen("https://ddragon.leagueoflegends.com/realms/na.json") as url:
    version = json.loads(url.read().decode())["n"]["champion"]
    print(version)


def get_champ(champion_id, version):
    with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion.json") as url:
        champs = json.loads(url.read().decode())["data"]

        for champ in champs.values():
            if champ["key"] == str(champion_id):
                return champ["id"]


def get_tips_against(champion):
    with urllib.request.urlopen(
            "http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion/" + champion + ".json") as url:
        data = json.loads(url.read().decode())

        tip = {}

        for count, tips in enumerate(data["data"][champion]["enemytips"]):
            name = champion + str(count + 1)
            tip[name] = str(count + 1) + ". " + tips
        
        return tip

def get_cooldowns(champion):
    with urllib.request.urlopen(
            "http://ddragon.leagueoflegends.com/cdn/" + version + "/data/en_US/champion/" + champion + ".json") as url:
        data = json.loads(url.read().decode())

        cooldowns = {}

        for count, spell in enumerate(data["data"][champion]["spells"]):
            cooldowns[count] = spell["cooldownBurn"]
        
        return cooldowns


api_key = "RGAPI-593ec73e-a75d-47b2-8276-d4e48cc98d54"

summoner = input("Your summoner name: ").replace(" ", "+")
tips = {}
spells = "QWER"

try:
    with urllib.request.urlopen(
            "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner + "?api_key=" + api_key) as url:
        userID = json.loads(url.read().decode())["id"]

    with urllib.request.urlopen(
            "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + userID + "?api_key=" + api_key) as url:
        for count, player in enumerate(json.loads(url.read().decode())["participants"]):
            if count == 0:
                print("\nTeam 1:")
            elif count == 5:
                print("\nTeam 2:")
            print(player["summonerName"] + " (" + get_champ(player["championId"], version) + ")")
            tips = get_tips_against(get_champ(player["championId"], version))
            cooldowns = get_cooldowns(get_champ(player["championId"], version))

            for count, cd in enumerate(cooldowns.values()):
                print(spells[count] + ": " + cd)
            for tip in tips.values():
                print(tip)
            if not bool(tips):
                print("No tips found for " + get_champ(player["championId"], version))
except urllib.error.HTTPError:
    print("The summoner you searched for is not in an active game")