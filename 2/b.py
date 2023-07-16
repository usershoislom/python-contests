a = int(input())
b = int(input())

alphabet = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', \
    'zeta', 'eta', 'theta', 'iota', 'kappa']

digits = ['I', 'II', 'III', 'IV', 'V', \
        'VI', 'VII', 'VIII', 'IX', 'X', \
        'XI', 'XII', 'XIII', 'XIV', 'XV', \
        'XVI', 'XVII', 'XVIII', 'XIX', \
        'XX', 'XXI', 'XXII', 'XXIII', \
        'XXIV', 'XXV', 'XXVI', 'XXVII', \
        'XXVIII', 'XXIX', 'XXX']
        
for i in range(a):
    row = ''
    for j in range(b):
        cell = alphabet[i] + '_' + digits[j]
        row += cell + ' '
    print(row[:-1])