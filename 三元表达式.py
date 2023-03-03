if __name__ == "__main__":
    pi = [3, 14, 15, 9, 26, 5, 35, 8, 97, 932]
    event_count = 0
    for i in pi:
        event_count += 1 if i % 2 == 0 else 0
    assert event_count == 4