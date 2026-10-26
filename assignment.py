# You can remove 'pass' if you written code in the function
# Exercise 1
def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    total = 0
    count = 0
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        score = int(parts[1])
        total += score
        count += 1
    file.close()
    if count == 0:
        return 0
    return round(total / count, 1)

# Exercise 3
def filter_passed(source, destination, pass_mark):
    f_src = open(source, "r")
    lines = f_src.readlines()
    f_src.close()
    passed_count = 0
    passed_lines = []
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split(",")
        score = int(parts[1])
        if score >= pass_mark:
            passed_lines.append(line.strip() + "\n")
            passed_count += 1
    f_dest = open(destination, "w")
    f_dest.writelines(passed_lines)
    f_dest.close()
    return passed_count

# Exercise 4
def replace_word(filename, old_word, new_word):
    # Write your code here
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
