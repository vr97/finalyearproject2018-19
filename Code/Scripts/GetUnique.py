
def get_unique_elements(list_of_elements, param) -> list:
    """
    Function to remove the redundant tweets in the list
    :param param: the parameter on which the dictionary should be sorted
    :param list_of_elements: takes in list of elements where each element is a dictionary
    :return returns the unique list of elements
    """
    my_dict = {iterator[param]: iterator for iterator in reversed(list_of_elements)}
    unique_list_of_tweets = list(my_dict.values())
    return unique_list_of_tweets

