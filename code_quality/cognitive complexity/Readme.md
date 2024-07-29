When discussing cognitive complexity in functions, it's essential to understand that the term refers to how difficult a piece of code is to understand and maintain. High cognitive complexity can make code harder to read, understand, and modify. Here are some strategies to keep the cognitive complexity of functions low:

1. **Single Responsibility Principle**: Each function should perform a single, well-defined task. This makes the function easier to understand and less prone to bugs.

2. **Clear Naming**: Use descriptive names for functions and variables. The purpose of a function should be evident from its name, reducing the need to delve into the implementation to understand what it does.

3. **Avoid Nested Logic**: Deeply nested conditionals and loops can make code difficult to follow. Try to flatten nested structures by breaking them into smaller functions or using guard clauses.

4. **Limit Function Size**: Keep functions short. If a function becomes too long, it’s often a sign that it should be refactored into smaller, more manageable functions.

5. **Use Early Returns**: Instead of nesting code inside multiple `if` statements, use early returns to handle edge cases and reduce nesting.

6. **Modularize Code**: Break down complex logic into smaller, reusable components. This can make the code more modular and easier to test and maintain.

7. **Avoid Side Effects**: Functions should avoid changing global state or relying on external variables. Functions that have no side effects (pure functions) are easier to reason about.

8. **Refactor Regularly**: Periodically review and refactor code to simplify complex functions and improve readability.

9. **Comment Wisely**: While code should be as self-explanatory as possible, use comments to clarify complex sections, but avoid over-commenting. Comments should explain why something is done, not what is done.

10. **Consistent Style**: Follow consistent coding conventions and styles. Consistent indentation, naming conventions, and code structure make it easier to understand and maintain the code.

By adhering to these practices, you can manage and reduce the cognitive complexity of your functions, making your codebase more maintainable and easier to work with.