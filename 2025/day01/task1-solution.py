def main():
  dial = 50
  zero_count = 0

  with open("input.txt") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue

      direction = line[0]   # 'L' or 'R'
      value = int(line[1:]) # number after

      if direction == 'R':
        dial = (dial + value) % 100
      else:
        dial = (dial - value) % 100

      if dial == 0:
        zero_count += 1
  print("Password:", zero_count)

if __name__ == "__main__":
    main()
