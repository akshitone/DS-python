

def test_location(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


def locate_card(cards, query):
    low, high = 0, len(cards) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            print("count:", count)
            return mid
        elif result == "right":
            low = mid + 1
        else:
            high = mid - 1
        count += 1
    return -1


if __name__ == "__main__":
    cards = [9, 8, 7, 6, 3, 2, 1]
    query = 9
    print(locate_card(cards, query))
