import random


class PaoYingShub:
  """
  You only need to put a name to play this game.
  """

  def __init__(self, player_name):
    self.player_name = player_name
    self.options = ["rock", "paper", "scissor"]
    self.isStart = False
    self.scores = {
      'player': 0,
      'bot': 0,
    }

  def start(self):
    self.isStart = True

    while self.isStart:
      try:
        player_select = int(self.menu())

        if player_select == 4:
          self.stop()

        elif player_select <= 3 and player_select >= 1:
          bot = random.choice(self.options)  # random value in list
          # get value from self.options
          player = self.options[player_select - 1]
          player_win = self.check_winner(player=player, bot=bot)

          print(f"player choice: {player}\nbot choice: {bot}")

          if player_win:
            print('player win🎉')
            self.scores['player'] += 1

          elif player_win == None:
            print("tie 😄")

          else:
            print("player lose🥲")
            self.scores['bot'] += 1

          self.score_board()

      except:
        print("Please only select choice below.")

  def stop(self):
    self.score_board()

    if self.scores['player'] > self.scores['bot']:
      print("You win this game!!💪")

    else:
      print("You lose this game, Robot will take over the world!! PuPeepPuPeep 🤖🦾")

    self.isStart = False

  def menu(self):
    print("[1] rock\n[2] paper\n[3] scissor\n[4] quit\n")
    return input("your choice?: ")

  def check_winner(self, player, bot):
    """
    This method will return True when player win bot, False when player lose and None when tie.
    """
    if player == 'rock' and bot != 'rock':
      if bot != 'scissor':
        return False
      return True
    elif player == 'paper' and bot != 'paper':
      if bot != 'rock':
        return False
      return True
    elif player == 'scissor' and bot != 'scissor':
      if bot != 'paper':
        return False
      return True
    else:
      return None

  def score_board(self):
    print(
      f'score:\nplayer🥷 {self.player_name}: {self.scores["player"]}\nbot🤖: {self.scores["bot"]}\n')


if __name__ == '__main__':
  game = PaoYingShub('Mos')
  game.start()
