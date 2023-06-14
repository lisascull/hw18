def cache(func):
    cache_dict = {}
    def wrapper(*a, **b):
        key = (a, frozenset(b.items()))
        if key in cache_dict:
            print('Result retrieved from cache.')
            return cache_dict[key]
        else:
            print('Executing function and caching the result.')
            result = func(*a, **b)
            cache_dict[key] = result
            return result

    return wrapper
@cache
def triangle_area(a, b):
    print('Виклик функції triangle_area')
    return 0.5 * a * b
print(triangle_area(5, 10))
print(triangle_area(5, 10))
