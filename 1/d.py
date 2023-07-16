import sys
 
coord = 10**6
 
print(f"? {-coord} {-coord}\n")
sys.stdout.flush()
dist_1 = int(input())
 
 
print(f"? {coord} {-coord}\n")
sys.stdout.flush()
dist_2 = int(input())
   
x = int((dist_1 - dist_2) / 2)
y = int(dist_1 - x - 2 * coord)

print(f"! {x} {y}\n")
sys.stdout.flush()
