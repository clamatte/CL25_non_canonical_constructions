import re

# Define the function to normalize text
def normalize_text(text):
    """text cleaning just for whitespaces and amc sentence markers"""
    # remove <s>
    text = re.sub(r'<s>', '', text)
    text = re.sub(r'</s>', '', text)
    # remove superfluous white spaces
    text = text.strip()
    return text



def split_and_explode(df, column, delimiters):
    """
    Splits and explodes a DataFrame column by a list of delimiters.

    Parameters:
    - df (DataFrame): The DataFrame to process.
    - column (str): The name of the column to split and explode.
    - delimiters (list): A list of regex patterns to split on.

    Returns:
    - DataFrame: A new DataFrame with the text split and exploded.
    """
    df_result = df.copy()
    current_column = column

    # Iterate through each delimiter and apply split and explode
    for i, delimiter in enumerate(delimiters):
        # Split the text by the current delimiter
        new_column = f"{current_column}_split_{i}"
        df_result[new_column] = df_result[current_column].str.split(delimiter)
        df_result = df_result.explode(new_column)
        current_column = new_column

    return df_result.rename(columns={current_column: 'final_split'})