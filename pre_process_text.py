'''
Pre process text
'''
def pre_process_text(text, window_size):
    '''
    This function breaks down the text into a list of "window size" number of sentences at a 
    '''
    list_answer = []
    sentence_stoppers = ['.','?','!']
    index_of_string = 0 
    while (index_of_string < len(text)):
        counter = 0
        window_string = ""
        while counter < window_size:
            if (index_of_string >= len(text)):
                break
            else:
                if (text[index_of_string] in sentence_stoppers):
                    counter += 1
                else:
                    pass
            window_string += (text[index_of_string])
            index_of_string += 1
        list_answer.append(window_string)
    return(list_answer)

if __name__ == '__main__':
    text_sample = "Snakes are elongated, legless reptiles belonging to the suborder Serpentes. They are found in diverse habitats around the world, ranging from deserts to rainforests. Snakes have a flexible body and can move quickly, enabling them to catch prey and escape from predators. They have a unique adaptation for killing prey - their jaws are hinged and can be opened wide, allowing them to swallow prey much larger than their head. Some species of snakes are venomous and their bite can be dangerous to humans, but many are harmless. Snakes play important roles in the ecosystems in which they live, serving as both predator and prey. yqsssss"
    ans = pre_process_text(text_sample,3)
    print(ans)