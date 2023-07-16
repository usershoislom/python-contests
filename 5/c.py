with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    password = f_in.readline().strip()
    has_upper = False
    has_lower = False
    has_digit = False
    num_digits = 0

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
            num_digits += 1

    is_strong = has_upper and has_lower and has_digit
    is_memorable = num_digits <= 3 and len(password) <= 10

    f_out.write('YES\n' if is_strong else 'NO\n')
    f_out.write('YES\n' if is_memorable else 'NO\n')

