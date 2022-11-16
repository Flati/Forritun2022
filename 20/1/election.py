results = {}
while True:
    data = input("Candidate and votes: ")
    if data == '':
        break
    data = data.split(' ')
    try:
        votes = int(data[1])
    except:
        print('Invalid no. of votes!')
        continue
    president = data[0].lower()
    if president in results:
        results[president] += votes
    else:
        results[president] = votes
sum = 0
for k in results:
    print(k + ': ' + str(results[k]))
    sum += results[k]
print('Total no. of votes:', sum)
