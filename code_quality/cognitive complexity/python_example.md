Let's walk through an example to illustrate the principles of managing cognitive complexity in functions.

### Example Scenario

Imagine we have a function that processes a list of transactions to calculate the total amount for a specific category, with additional considerations for certain types of transactions.

### High Cognitive Complexity Function

Here’s a function with high cognitive complexity due to deeply nested conditionals and long logic:

```python
def calculate_total_amount(transactions, category):
    total = 0
    for transaction in transactions:
        if transaction['category'] == category:
            if transaction['type'] == 'credit':
                if transaction['amount'] > 1000:
                    total += transaction['amount'] * 1.1  # 10% bonus for high credits
                else:
                    total += transaction['amount']
            elif transaction['type'] == 'debit':
                if transaction['amount'] < 100:
                    total -= transaction['amount'] * 0.9  # 10% discount for low debits
                else:
                    total -= transaction['amount']
            else:
                # Handle other transaction types
                pass
        else:
            # Ignore transactions not in the desired category
            pass
    return total
```

### Refactored Low Cognitive Complexity Function

Let’s refactor this function by breaking it into smaller, more manageable functions, applying the principles mentioned:

1. **Single Responsibility**: Each function should handle one aspect of the problem.
2. **Clear Naming**: Use descriptive names.
3. **Avoid Nested Logic**: Reduce nesting by using early returns and separate concerns.

```python
def calculate_total_amount(transactions, category):
    total = 0
    for transaction in transactions:
        if transaction['category'] != category:
            continue
        total += process_transaction(transaction)
    return total

def process_transaction(transaction):
    if transaction['type'] == 'credit':
        return process_credit(transaction)
    elif transaction['type'] == 'debit':
        return process_debit(transaction)
    else:
        return 0

def process_credit(transaction):
    if transaction['amount'] > 1000:
        return transaction['amount'] * 1.1  # 10% bonus for high credits
    else:
        return transaction['amount']

def process_debit(transaction):
    if transaction['amount'] < 100:
        return -transaction['amount'] * 0.9  # 10% discount for low debits
    else:
        return -transaction['amount']
```

### Explanation of Refactoring

1. **Function Decomposition**: 
   - `calculate_total_amount` focuses on iterating through transactions and determining if they belong to the specified category.
   - `process_transaction` delegates the processing based on the transaction type.
   - `process_credit` and `process_debit` handle the specific calculations for credits and debits, respectively.

2. **Early Returns**:
   - By using `continue` in `calculate_total_amount`, we skip processing transactions that don’t match the category.

3. **Simplified Logic**:
   - Each helper function (`process_credit`, `process_debit`) has a clear and straightforward responsibility, reducing nested conditions and improving readability.

4. **Clear Naming**:
   - Function names clearly describe their purpose, making the code easier to follow without needing extensive comments.

By breaking the logic into smaller, purpose-driven functions, we’ve reduced the cognitive load required to understand each piece of code. Each function is easier to read, test, and maintain, which contributes to a lower overall cognitive complexity.