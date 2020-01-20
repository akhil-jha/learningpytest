import sample2

# If the file values of "letters.txt" have been deleted, the count of the alphabet will not be 26.
def test_check_file():
    file = open("letters.txt", "r")
    count = 0
    for _ in file.readlines():
        count = count + 1
    assert count == 26