def main():
  dial = 50
  zero_count = 0

  with open("input.txt") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue

      direction = line[0]   # 'L' or 'R'
      value = int(line[1:]) # number of clicks

      # Determine step: +1 for right, -1 for left
      step = 1 if direction == 'R' else -1

      for _ in range(value):
        dial = (dial + step) % 100  # move one click
        if dial == 0:
            zero_count += 1
  print("Password (method 0x434C49434B):", zero_count)

if __name__ == "__main__":
    main()
