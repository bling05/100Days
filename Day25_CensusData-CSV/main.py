import pandas

def main():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_data.csv")

    data_gray = data[data['Primary Fur Color'] == 'Gray']
    data_cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
    data_black = data[data['Primary Fur Color'] == 'Black']

    dict = {'Fur Color': ['gray', 'cinnamon', 'black'], 
            'Count': [len(data_gray), len(data_cinnamon),  len(data_black)]}

    pandas.DataFrame(dict).to_csv("squirrel_count.csv")

if __name__ == '__main__':
    main()
