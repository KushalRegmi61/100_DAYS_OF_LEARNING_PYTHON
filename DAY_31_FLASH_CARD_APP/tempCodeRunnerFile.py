def pop_card():
    next_card()
    global new_card
    new_data_dict = {new_data for new_data in data_list if new_data["English"] != new_card["English"]}
    words_to_learn = pandas.DataFrame(new_data_dict)
    words_to_learn.to_csv(r"E:\python\DAY_31_FLASH_CARD_APP\data\words_to_learn.csv", index= False)