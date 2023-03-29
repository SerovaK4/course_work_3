from pprint import pprint
from utils import get_data, get_filtrate_data, get_last_values, get_formed_data


def main():
    COUNT_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data = get_data()
    data = get_filtrate_data(data, FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_VALUES)
    data = get_formed_data(data)

    for row in data:
        print(row, end='\n')


if __name__ == "__main__":
    main()