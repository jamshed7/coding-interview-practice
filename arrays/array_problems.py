
#Function to check anagram

#fast and easy solution
def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

#more optimized solution
def anagram2(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2. replace(' ', '').lower()

    #counting dictionary
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

def anagram3(s1,s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    sentence2 = list(s1)

    for char in s2:
        if char in sentence2:
            sentence2.remove(char)

    if len(sentence2) == 0:
        return True
    else:
        return False


#my solution
def pair_sum(arr,k):

    result = []

    n = len(arr)

    for item1 in range(n):
        for item2 in range(item1, n):
            if arr[item1]+arr[item2] == k:
                result.append((arr[item1],arr[item2]))

    result = set(result)

    return len(result)


#optimal solution O(n)
def pair_sum(arr,k):

    if len(arr)<2:
        return

    seen = set()
    output = set()


    for item in arr:
        target = k - item

        if target not in seen:
            seen.add(item)
        else:
            output.add( ( min(item, target), max(item, target) ) )

    return len(output)




##find the missing element
def finder(arr1,arr2):

    #counting dictionary
    count = {}

    for num in arr1:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr2:
        if num in arr2:
            count[num] -= 1
        else:
            count[num] = 1

    for k in count:
        if count[k] != 0:
            return k

    return



##largest continuous sum problem
def large_cont_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


##setence reversal
def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        # If element isn't a space
        if s[i] not in spaces:
            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))
