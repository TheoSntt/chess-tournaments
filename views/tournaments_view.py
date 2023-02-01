"""Base view."""


class TournamentsView:
    """Card game view."""

    def __init__(self):
        self.MAIN_MENU_PROMPT = ("Que voulez-vous faire ?\n"
                                 "1 - Imprimer des rapports\n"
                                 "2 - Ajouter des joueurs à la base de donnée\n"
                                 "3 - Créer un tournoi\n"
                                 "4 - Continuer un tournoi en cours")
        self.MAIN_MENU_VALUES = [1, 2, 3, 4]

        # def validate_user_input(self, input, accepted_values):
    #     """Check if the user imput is one of the expected values"""
    #     if input in accepted_values:
    #         return True
    #     return False

    def get_correct_input(self, prompt, accepted_values):
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Veuillez choisir une des options proposées.")
                continue
            if value not in accepted_values:
                print("Veuillez choisir une des options proposées.")
                continue
            else:
                break
        return value

    def prompt_main_menu(self):
        """Prompt app main menu."""
        while not self.validate_user_input(user_choice, [1, 2, 3, 4]):
            user_choice = input("Que voulez-vous faire ?\n"
                                "1 - Imprimer des rapports\n"
                                "2 - Ajouter des joueurs à la base de donnée\n"
                                "3 - Créer un tournoi\n"
                                "4 - Continuer un tournoi en cours")

            return user_choice

    def prompt_for_player(self):
        """Prompt for a name."""
        name = input("tapez le nom du joueur : ")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        """Show the player hand."""
        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")

    def prompt_for_flip_cards(self):
        """Request to return the cards."""
        print()
        input("Prêt à retourner les cartes ?")
        return True

    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True