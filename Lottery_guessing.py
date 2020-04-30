import random

f = open('Weights_Holder.csv', 'r+')
f.close()


class wei:
    listy = [19, 30, 44, 56, 65, 24]
    min_begin = .7
    max_end = 1.3
    weights = []
    locations = []


def search(userInput, data_base_d):
    counter = 0
    location = int
    for _ in data_base_d:
        if userInput == data_base_d[counter]:
            location = counter
        counter += 1
    if location != int:
        return location
    return


def formatting_from_csv():
    fil = open('LottoryData.csv', 'r+')
    fil_read = fil.read()
    holding_list = fil_read.split('\n')
    proper_list = []
    counter = 0
    for _ in holding_list:
        holder = holding_list[counter][13:]
        holder.split(',')
        proper_list.append(holder[0:2])
        proper_list.append(holder[3:5])
        proper_list.append(holder[6:8])
        proper_list.append(holder[9:11])
        proper_list.append(holder[12:14])
        proper_list.append(holder[15:17])
        counter += 1
    fil.close()
    return proper_list, len(proper_list) / 6


def roll():
    min_mute = wei.min_begin * 10
    max_mut = wei.max_end * 10
    size_list = []
    counter = 1
    size_list.append(min_mute)
    while size_list[-1] < max_mut:
        size_list.append(min_mute + counter)
        counter += 1
    random.shuffle(size_list)
    ret = size_list[0]
    ret /= 10
    return ret


def data_base(finalResult):
    with (open('Weights_Holder.csv', "a")) as fi:
        counter = 0
        for _ in finalResult:
            fi.write(str(finalResult[counter]) + ',')
            counter += 1
        fi.write('\n')


def guesser():
    counter = 0
    holder = []
    for _ in wei.listy:
        holder.append(roll())
        wei.listy[counter] = wei.listy[counter] * holder[-1]
        wei.listy[counter] = int(wei.listy[counter])
        counter += 1
    return wei.listy, holder


def load_random_guess():
    guess_list, weight_list = guesser()
    load_y_list, len_list_y_six = formatting_from_csv()
    load_search_list = []
    holder = 0
    counter = 0 + (6 * holder)
    results = []
    result_position = []
    counter_int = 0
    while counter_int < 396:
        load_y_list[counter_int] = int(load_y_list[counter_int])
        counter_int += 1
    while holder < 396:
        place_holder_ = 0
        while place_holder_ < 6:
            load_search_list.append(load_y_list[counter])
            place_holder_ += 1
            holder += 1
            counter += 1
        counter_two = 0
        for _ in load_search_list:
            if guess_list[counter_two] == load_search_list[counter_two]:
                results.append((guess_list[counter_two]))
                result_position.append(counter_two * 10)
            counter_two += 1
        load_search_list = []
    if results:
        counter_three = 0
        for _ in results:
            location = search(results[counter_three], guess_list)
            results[counter_three] = int(weight_list[location] * 10)
            counter_three += 1
        counter_three = 0
        for _ in result_position:
            results.append(int(result_position[counter_three]))
            counter_three += 1
        data_base(results)


def sort_weights():
    file = open('Weights_Holder.csv', "r+")
    file_read = file.read()
    holding_list = file_read.split('\n')
    counter = 0
    for _ in holding_list:
        formatting = holding_list[counter].split(',')
        formatting.remove(formatting[-1])
        middle_of_formatting = len(formatting) / 2
        counter_format = 0
        for _ in formatting:
            if counter_format < middle_of_formatting:
                wei.weights.append(float(formatting[counter_format]) / 10)
                counter_format += 1
            else:
                formatting[counter_format] = int(formatting[counter_format])
                wei.locations.append(int(formatting[counter_format] / 10))
                counter_format += 1
        counter += 1
    file.close()


def predict():
    counter = 0
    pos_zero = 1
    pos_one = 1
    pos_two = 1
    pos_three = 1
    pos_four = 1
    pos_five = 1
    positions = [pos_zero, pos_one, pos_two, pos_three, pos_four, pos_five]
    for _ in wei.locations:
        if wei.locations[counter] == 0:
            pos_zero *= wei.weights[counter]
        if wei.locations[counter] == 1:
            pos_one *= wei.weights[counter]
        if wei.locations[counter] == 2:
            pos_two *= wei.weights[counter]
        if wei.locations[counter] == 3:
            pos_three *= wei.weights[counter]
        if wei.locations[counter] == 4:
            pos_four *= wei.weights[counter]
        if wei.locations[counter] == 5:
            pos_five *= wei.weights[counter]
        counter += 1
    counter = 0
    for _ in wei.listy:
        wei.listy[counter] *= positions[counter]
        counter += 1
    print(wei.listy)


load_random_guess()
sort_weights()
predict()
