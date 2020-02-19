
aliens = []
for aliens_number in range(30):
    new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print(f'Total num of aliens: {len(aliens)}')

for alien in aliens[0:6]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'

for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

for alien in aliens[0:7p]:
    print(alien)
print('...')