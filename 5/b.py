def print_i(m):
    print("*   * " * m)
    print("*  ** " * m)
    print("* * * " * m)
    print("**  * " * m)
    print("*   * " * m)    
    print()

n = int(input())
m = int(input())

for i in range(n):
    print_i(m)