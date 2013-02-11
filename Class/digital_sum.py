def can_pay_with_two_coins(denoms, amount):
    for i in range(len(denoms)):
        for j in range(len(denoms)):
            if (denoms[i] + denoms[j]) % amount == 0:
                return True
    return False
