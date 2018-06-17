def sochanle(n):

    result = []

    for i in range(n):
        if i % 2 == 1:
            result.append(-1)
        else:
            result.append(2 - i * 0.25)

        return result



