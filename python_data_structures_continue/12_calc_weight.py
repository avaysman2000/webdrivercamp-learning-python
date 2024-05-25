#!/usr/bin/python3
def calc_weight(list_=[]):

    if not list_:  # If the list is empty, return 0
        return 0
    
    weighted_sum = sum(score * weight for score, weight in list_)  # Calculate the weighted sum
    sum_weights = sum(weight for _, weight in list_)  # Calculate the sum of weights
    
    return weighted_sum / sum_weights  # Calculate and return the weighted average

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
