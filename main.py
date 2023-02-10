def main(num): # n mustn't be 2 or 5
    # https://en.wikipedia.org/wiki/Reciprocals_of_primes - inspired by William Shanks
    if num == 2 or num == 5:
        return "there is no loop to be found"

    elif num == 3:
        return 1
    
    else:
        k = len(str(num))-1

        rests = [10**(k+1)]
        Loop = False
        index = 0

        while Loop == False:
            if index == 0:
                rest = (rests[0]%num)*10
                rests.append(rest)

                if rests[1] == rests[0]:
                    return index
                    Loop = True
                else:
                    index += 1
            
            elif index != 0:
                rest = (rests[index]%num)*10
                rests.append(rest)

                if rests[index] == rests[0]:
                    return index
                    Loop = True
                else:
                    index += 1