import secrets

deck = list(range(1, 53))

hand = secrets.SystemRandom().sample(deck, k=5)
print(hand)
