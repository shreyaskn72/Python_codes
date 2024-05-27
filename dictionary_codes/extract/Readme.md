# Extract Dictionaries Based on Common ID

This Python script extracts dictionaries from a large list (`list1`) based on a common key ('id' in `list1` and 'specific_id' in `list2`) with a smaller list (`list2`).

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script file (`extract_dictionaries.py`).
3. Open the script file in your preferred text editor or IDE.

## Instructions

1. Modify the `list1` and `list2` variables in the script to contain your desired lists of dictionaries.
2. Run the script. It will extract dictionaries from `list1` where the 'id' is common in `list2`.
3. The filtered dictionaries will be displayed as the output.

## Example

Consider the following sample lists of dictionaries:

```python
list1 = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Alice'},
    {'id': 3, 'name': 'Bob'},
    # More dictionaries...
]

list2 = [
    {'specific_id': 1},
    {'specific_id': 3}
]
```
Running the script will result in the following output:

Filtered List 1:
```python
[{'id': 1, 'name': 'John'}, {'id': 3, 'name': 'Bob'}]
```
