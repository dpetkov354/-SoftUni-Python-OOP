from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player(self, player: Player):
        current_player = [u.name for u in self.players if u.name == player.name]
        if current_player:
            return current_player[0]

    def find_player_by_name(self, name: str):
        current_player = [u for u in self.players if u.name == name]
        if current_player:
            return current_player[0]
        else:
            return None

    def find_sustenance(self, sustenance_name: str):
        sustenance = [u for u in self.supplies if u.__class__.__name__ == sustenance_name]
        if sustenance:
            return sustenance[-1]
        else:
            if sustenance == "Food":
                raise Exception("There are no food supplies left!")
            elif sustenance == "Drink":
                raise Exception("There are no drink supplies left!")

    def add_player(self, *args):
        added_players = []
        for arg in args:
            if arg in self.players:
                continue
            else:
                self.players.append(arg)
                added_players.append(arg.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        added_supplies = []
        for arg in args:
            added_supplies.append(arg.name)
            self.supplies.append(arg)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_player_by_name(player_name)

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food" or sustenance_type == "Drink":
            if player is not None:
                sustenance = self.find_sustenance(sustenance_type)
                if sustenance is not None:
                    index_value_of_sustenance = len(self.supplies) - self.supplies[::-1].index(sustenance) - 1
                else:
                    if sustenance_type == "Food":
                        raise Exception("There are no food supplies left!")
                    else:
                        raise Exception("There are no drink supplies left!")

                if player.stamina == 100:
                    return f"{player_name} have enough stamina."
                if player.stamina + sustenance.energy > 100:
                    player.stamina = 100
                    self.supplies.pop(index_value_of_sustenance)
                    return f"{player_name} sustained successfully with {sustenance.name}."

                else:
                    player.stamina += sustenance.energy
                    self.supplies.pop(index_value_of_sustenance)
                    return f"{player_name} sustained successfully with {sustenance.name}."
            else:
                pass
        else:
            pass

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\nPlayer {second_player.name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina > second_player.stamina:
            first_player.stamina -= second_player.stamina / 2
            if first_player.stamina <= 0:
                return f"Winner: {second_player.name}"
            second_player.stamina -= first_player.stamina / 2

        elif second_player.stamina > first_player.stamina:
            second_player.stamina -= first_player.stamina / 2
            if second_player.stamina <= 0:
                return f"Winner: {first_player.name}"
            first_player.stamina -= second_player.stamina / 2

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        elif second_player.stamina > first_player.stamina:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            if (player.stamina - player.age*2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age*2

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")
        for supply in self.supplies:
            result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")
        return '\n'.join(result)
