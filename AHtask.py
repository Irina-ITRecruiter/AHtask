import csv

name = input('Enter your name: ')
email = input('Enter your email: ')

print('You just entered %s, %s, is it correct?'%(name, email))
save = input('Save to CSV? ')

if save == 'yes':
	file = open('results.csv', 'a') 
	csv_writer = csv.writer(file) 
	csv_writer.writerow([name, email])