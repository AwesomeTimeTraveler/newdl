import random

# Card classes
class Card:
    def __init__(self, name, card_type, effect=None, stats=None):
        self.name = name
        self.card_type = card_type
        self.effect = effect
        self.stats = stats

class CharacterCard(Card):
    def __init__(self, name, effect, stats):
        super().__init__(name, "Character", effect, stats)

class ItemCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, "Item", effect)

class ToolCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, "Tool", effect)

class QuestCard(Card):
    def __init__(self, name, effect):
        super().__init__(name, "Quest", effect)

# Player class
class Player:
    def __init__(self, username):
        self.username = username
        self.hand = []
        self.field_card = None
        self.deck = []
        self.graveyard = []
        self.out_of_bounds = []
        self.quest_zone = []

# Game Engine
class GameEngine:
    def __init__(self):
        self.players = []
        self.current_turn = None
        self.game_state = "waiting"

    def add_player(self, player):
        if len(self.players) < 2:
            self.players.append(player)
            return True
        return False

    def start_game(self):
        self.game_state = "in-progress"
        self.current_turn = random.randint(0, 1)
        for player in self.players:
            self.draw_cards(player, 4)
        self.reveal_field_cards()

    def draw_cards(self, player, num_cards):
        for _ in range(num_cards):
            if len(player.deck) > 0:
                card = player.deck.pop(0)
                player.hand.append(card)

    def reveal_field_cards(self):
        for player in self.players:
            if len(player.deck) > 0:  # Check if the deck is empty
                player.field_card = player.deck.pop()

    # Gameplay stages
    def draw_stage(self):
        for player in self.players:
            self.draw_cards(player, 1)
        # TODO: Additional logic if needed

    def stand_by_stage(self):
        # No specific actions occur during this stage
        pass

    def quest_stage(self, player, quest_card):
        # TODO: Validate that quest_card is a Quest Card
        player.quest_zone.append(quest_card)

    def main_stage(self, player, character_card=None, item_cards=[], tool_cards=[]):
        # TODO: Implement main stage logic here, involving character, item, and tool cards
        pass

    def end_stage(self):
        self.current_turn = 1 - self.current_turn  # Toggle between 0 and 1

    # Other methods
    def is_valid_deck(self, deck):
        # Add logic to validate the deck
        return True

    def setup_player_deck(self, player, deck):
        if self.is_valid_deck(deck):
            player.deck = deck
            player.field_card = deck[-1]
            return True
        return False

# Create some cards and players for testing
card1 = CharacterCard("Warrior", "None", {"Attack": 5, "Health": 10, "Speed": 2, "Capacity": 1})
card2 = ItemCard("Sword", "Increase Attack by 2")
field_card = Card("Castle", "Field")

# Add more cards for testing
card3 = CharacterCard("Mage", "None", {"Attack": 3, "Health": 6, "Speed": 3, "Capacity": 0})
card4 = ItemCard("Potion", "Increase Health by 2")

player1 = Player("Alice")
player1.deck = [card1, card2, card3, card4, field_card]  # Added more cards

player2 = Player("Bob")
player2.deck = [card1, card2, card3, card4, field_card]  # Added more cards

# Initialize game engine and add players
game = GameEngine()
game.add_player(player1)
game.add_player(player2)

# Setup player decks and start the game
game.setup_player_deck(player1, player1.deck)
game.setup_player_deck(player2, player2.deck)
game.start_game()

# Simulating gameplay stages for player 1
game.draw_stage()
game.stand_by_stage()
game.quest_stage(player1, QuestCard("Find Gem", "Reward: Draw 2 cards"))
game.main_stage(player1, character_card=card1, item_cards=[card2])
game.end_stage()
