def get_score(dice):
  from collections import Counter

  if len(dice) == 1:
      dice.append(1000)
      dice.append(2000)
      dice.append(3000)
      dice.append(4000)
      dice.append(5000)
  elif len(dice) == 2:
      dice.append(1000)
      dice.append(2000)
      dice.append(3000)
      dice.append(4000)
  elif len(dice) == 3:
      dice.append(1000)
      dice.append(2000)
      dice.append(3000)
  elif len(dice) == 4:
      dice.append(1000)
      dice.append(2000)
  elif len(dice) == 5:
      dice.append(1000)

  score = 0
  new_score = 0

  sorted_dice = sorted(dice)

  cnt = Counter()
  for i in dice:
      cnt[i] += 1
  count_num_dict = dict(cnt)
  print count_num_dict

  if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
      new_score = 1000
      if new_score > score:
          score = new_score
  if sorted_dice[0] == sorted_dice[1] and sorted_dice[2] == sorted_dice[3] and sorted_dice[4] == sorted_dice[5] and sorted_dice[0] != sorted_dice[2]:
      new_score = 750
      if new_score > score:
          score = new_score
  if 1 in count_num_dict and count_num_dict[1] == 3:
      new_score = 1000

      if 2 in count_num_dict and count_num_dict[2] == 3:
        new_score += 200
      if 3 in count_num_dict and count_num_dict[3] == 3:
        new_score += 300
      if 4 in count_num_dict and count_num_dict[4] == 3:
        new_score += 400
      if 5 in count_num_dict and count_num_dict[5] == 3:
        new_score += 500
      elif 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if 6 in count_num_dict and count_num_dict[6] == 3:
        new_score += 600
      if new_score > score:
          score = new_score
  if 2 in count_num_dict and count_num_dict[2] == 3:
      new_score = 200

      if 3 in count_num_dict and count_num_dict[3] == 3:
        new_score += 300
      if 4 in count_num_dict and count_num_dict[4] == 3:
        new_score += 400
      if 5 in count_num_dict and count_num_dict[5] == 3:
        new_score += 500
      elif 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if 6 in count_num_dict and count_num_dict[6] == 3:
        new_score += 600

      if 1 in count_num_dict:
        new_score += count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 3 in count_num_dict and count_num_dict[3] == 3:
      new_score = 300

      if 4 in count_num_dict and count_num_dict[4] == 3:
        new_score += 400
      if 5 in count_num_dict and count_num_dict[5] == 3:
        new_score += 500
      elif 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if 6 in count_num_dict and count_num_dict[6] == 3:
        new_score += 600

      if 1 in count_num_dict:
        new_score += count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 4 in count_num_dict and count_num_dict[4] == 3:
      new_score = 400

      if 5 in count_num_dict and count_num_dict[5] == 3:
        new_score += 500
      elif 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if 6 in count_num_dict and count_num_dict[6] == 3:
        new_score += 600

      if 1 in count_num_dict:
        new_score += count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 5 in count_num_dict and count_num_dict[5] == 3:
      new_score = 500
      if 1 in count_num_dict:
        new_score += count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 6 in count_num_dict and count_num_dict[6] == 3:
      new_score = 600
      if 1 in count_num_dict:
        new_score += count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 1 in count_num_dict and count_num_dict[1] == 4:
      new_score = 2000
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 2 in count_num_dict and count_num_dict[2] == 4:
      new_score = 400
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 3 in count_num_dict and count_num_dict[3] == 4:
      new_score = 600
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 4 in count_num_dict and count_num_dict[4] == 4:
      new_score = 800
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 5 in count_num_dict and count_num_dict[5] == 4:
      new_score = 1000
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 6 in count_num_dict and count_num_dict[6] == 4:
      new_score = 1200
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 1 in count_num_dict and count_num_dict[1] == 5:
      new_score = 3000
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 2 in count_num_dict and count_num_dict[2]== 5:
      new_score = 600
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 3 in count_num_dict and count_num_dict[3] == 5:
      new_score = 900
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 4 in count_num_dict and count_num_dict[4] == 5:
      new_score = 1200
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 5 in count_num_dict and count_num_dict[5] == 5:
      new_score = 1500
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if new_score > score:
          score = new_score
  if 6 in count_num_dict and count_num_dict[6] == 5:
      new_score = 1800
      if 1 in count_num_dict:
        new_score = count_num_dict[1] * 100
      if 5 in count_num_dict:
        new_score += count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  if 1 in count_num_dict and count_num_dict[1] == 6:
      new_score = 4000
      if new_score > score:
          score = new_score
  if 2 in count_num_dict and count_num_dict[2] == 6:
      new_score = 800
      if new_score > score:
          score = new_score
  if 3 in count_num_dict and count_num_dict[3] == 6:
      new_score = 1200
      if new_score > score:
          score = new_score
  if 4 in count_num_dict and count_num_dict[4] == 6:
      new_score = 1600
      if new_score > score:
          score = new_score
  if 5 in count_num_dict and count_num_dict[5] == 6:
      new_score = 2000
      if new_score > score:
          score = new_score
  if 6 in count_num_dict and count_num_dict[6] == 6:
      new_score = 2400
      if new_score > score:
          score = new_score
  if 1 in count_num_dict:
      new_score = count_num_dict[1] * 100
      if new_score > score:
          score = new_score
      if 5 in count_num_dict:
          new_score += count_num_dict[5] * 50
          if new_score > score:
              score = new_score
          print score
  if 5 in count_num_dict:
      new_score = count_num_dict[5] * 50
      if new_score > score:
          score = new_score
  print score

  if score == 0:
      return "Zonk"
  else:
      return score
