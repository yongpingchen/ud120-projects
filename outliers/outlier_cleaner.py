#!/usr/bin/python
import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    # predictions, ages, and net_worths is array of array, need to reshape
    predictions = np.array(predictions).reshape(-1)
    ages = np.array(ages).reshape(-1)
    net_worths = np.array(net_worths).reshape(-1)
    errors = abs(predictions-net_worths)
    idxs = np.argsort(errors)[:81]

    cleaned_data = zip(
        np.take(ages, idxs),
        np.take(net_worths, idxs),
        np.take(errors, idxs))

    return cleaned_data
