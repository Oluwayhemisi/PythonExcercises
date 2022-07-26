def get_digit(number: int, position: int) -> int:
    """
    return digit at position in number,counting from right
    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> 3 == 4
    false
    >>> "hello"
    'hello'

    """

    return number // (10**position) % 10