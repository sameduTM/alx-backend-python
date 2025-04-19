# 0x02. Python - Async Comprehension

## Description
This project focuses on asynchronous programming in Python, specifically using asynchronous comprehensions and generators. By the end of this project, you will have a solid understanding of how to write and use asynchronous generators and comprehensions, as well as how to type-annotate them.

---

## Learning Objectives
By completing this project, you should be able to:

- Write an **asynchronous generator**.
- Use **async comprehensions** effectively.
- Type-annotate generators and coroutines.

---

## Resources
To help you complete this project, refer to the following resources:

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

---

## Requirements
- **Editor**: vi, vim, emacs
- **Python Version**: Python 3.7
- **OS**: Ubuntu 18.04 LTS
- **Code Style**: Follow `pycodestyle` (version 2.5.x)
- All files must:
  - End with a new line.
  - Start with `#!/usr/bin/env python3`.
  - Include proper documentation for modules, functions, and coroutines.
  - Be type-annotated.

---

## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that:
- Loops 10 times.
- Asynchronously waits 1 second in each iteration.
- Yields a random number between 0 and 10.

**Example Usage**:
```python
#!/usr/bin/env python3

import asyncio
async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())