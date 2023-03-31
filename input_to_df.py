import pdf_text_extractor
import pre_process_text
import individual_window_breakdown
import pandas as pd

def input_to_df():
    file = input("Enter file path: ")
    window_size = int(input("How many sentences would you like to analyze at a time?: "))
    text = pdf_text_extractor.extract_text(file)
    los = pre_process_text.pre_process_text(text, window_size)
    dos = individual_window_breakdown.individual_window_breakdown(los)
    return(pd.DataFrame.from_dict(dos))

if __name__ == '__main__':
    print(input_to_df())