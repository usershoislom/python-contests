x_a = int(input())
y_a = int(input())

x_b = int(input())
y_b = int(input())

x_c = int(input())
y_c = int(input())

x_min = min(x_a, x_b)
x_max = max(x_a, x_b)
y_min = min(y_a, y_b)
y_max = max(y_a, y_b)

if (x_c < x_min or x_c > x_max) or (y_c < y_min or y_c > y_max):
        # print("in if\n")
        x_a = 2 * x_c - x_a
        y_a = 2 * y_c - y_a

        x_b = 2 * x_c - x_b
        y_b = 2 * y_c - y_b
    
        print(x_a, y_a, x_b, y_b)
else:
    print("False")
