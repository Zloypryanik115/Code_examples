from functools import reduce, wraps
from operator import add, getitem
import math
#def rotate(lst):
#    buff = lst[0]
#    lst[0] = lst[-1]
#    lst[-1] = buff
#    #lst[-1], lst[0] = lst[0], lst[-1]


#def rotate(lst):
#    if lst:
#        lst.insert(0, lst.pop())
#l = []
#rotate(l)
#print(l)

#a = [1,2,3,4,5]
#a= a[::-1]
##b[0] = 9
#print(a)
##print(b)

#def rotated_left(item):
#    return item[1:] + item[:1]
#
#def rotated_right(item):
#    return item[-1:] + item[:-1]
#
#print(rotated_left([1,2,3,4]))
#print(rotated_right([1,2,3,4]))
#original_list = [1,2,3,4]
#for x in original_list[:]:
#    print('x = ', x)
#    original_list.pop(0)
#    print(original_list)
#print(original_list)

#def search_long_string(source):
#    for item in source:
#        if len(item) >= 5:
#            return item
#        
#animals = ['cat', 'mole', 'tiger', 'lion', 'camel']
#cursor = iter(animals)
#print(search_long_string(animals))
#print(search_long_string(animals))
#print(search_long_string(cursor))
#print(search_long_string(cursor))
#print(search_long_string(cursor))
#print(search_long_string(cursor))

#def find_index(value, items):
#    for index, item in enumerate(items):
#        if item == value:
#            return index
##
##
#def find_second_index(value, items):
#    i_items = iter(items)
#    pos = find_index(value, i_items)
#    if pos is not None:
#        result = find_index(value, i_items)
#        if result is not None:
#            return result + pos + 1
#        
#        
#print(find_second_index('s', 'boocbss'))

#def find_second_index(value, items):
#    pos = find_index(value,items)
#    if pos is not None:
#        result = find_index(value, items[pos+1:])
#        if result is not None:
#            return result + pos + 1
#
#print(find_second_index('o', 'boob'))

#animals = ['cat', 'mole', 'tiger', 'lion', 'camel']
#for i, _ in enumerate(animals):
#    animals[i] = animals[i] + '!'
#    print(animals[i])
#print(animals)

#dict = {'foo': 'bar', 'baz': 42, 'items': {1: 'apple', 2: 'orange', 100500: 'lemon'}}
#for v in dict.values():
#    print(v)
#    v = str(v) + '1'
#    print(v)
#    
#print((', ').join(list(dict.keys())))
#
#dict2 = {'foo': 'bar', 'baz': 42}
#for k, v in dict2.items():
#    print(k,v)
#    k, v = v, k
#    print(k, v)
#
#print(dict2)
#
#def test(a, b):
#    return a,b
#print(test(5,4))
#print(type(test(5,4)))

#def make_user(name, age):
#    return {'name': name, 'age': age}
#
#def format_user(dict_user):
#    #return f'{dict_user['name']}, {dict_user['age']}'
#    return dict_user['name'] +', ' + str(dict_user['age'])
#
#vasya = make_user('Vasya', 44)
#print(vasya)
#print(format_user(vasya))

#c = "сцообакенц"
#d = ["cat", "dog", "cat"]
#def count_all(iter_item):
#    result = {}
#    for i in iter_item:
#        result[i] = 0
#    for i in iter_item:
#        if i in result:
#            result.update({i : result[i] + 1})
#
#    return result
#
#print(count_all("*" * 20))
#
#def count_all_1(items):
#    counters = {}
#    for item in items:
#        counters[item] = counters.get(item, 0) + 1
#    return counters
#
#print(count_all_1("*" * 20))


#def collect_indexes(iter_item):
#    result = {}
#    for index, elem in enumerate(iter_item):
#        result.setdefault(elem, []).append(index)
#    return result
#
#d = collect_indexes("hello")
#print(d)

#def all_unique(item):
#    return len(item) == len(set(item))

#def toggle(flag, flags):
#    if flag in flags:
#        flags.discard(flag)
#    else:
#        flags.add(flag)
#
#
#def toggled(flag, flags):
#    result = flags.copy()
#    if flag in flags:
#        result.remove(flag)
#    else:
#        result.add(flag)
#    return result

#def diff_keys(old_dict, new_dict):
#    kept = set(old_dict) & set(new_dict)
#    added = set(new_dict) - set(old_dict)
#    removed = set(old_dict) - set(new_dict)
#    return {'kept': kept, 'added': added, 'removed': removed}
#
#print(diff_keys({'name': 'Bob', 'age': 42}, {}))
#print(diff_keys({}, {'name': 'Bob', 'age': 42}))
#print(diff_keys({'a': 2}, {'a': 1}))


#def greet(name, *args):
#    if args:
#        return 'Hello, ' + name + ' and ' + (' and ').join(args) + '!'
#    return 'Hello, ' + name + '!'
#
#def greet_1(who, *args):
#    names = ' and '.join((who,) + args)
#    return 'Hello, {}!'.format(names)
#
#def rgb(red=0, green=0, blue=0):
#    return 'rgb({}, {}, {})'.format(red, green, blue)
#
#
#
#def get_colors():
#    result = {'red': rgb(red=255), 'green': rgb(green=255), 'blue': rgb(blue=255)}
#    return result


#def updated(target_dict, **kwargs):
#    new_dict = target_dict.copy()
#    new_dict.update(kwargs)
#    return new_dict

#def double(function):
#    def inner(argument):
#        return function(function(argument))
#    return inner
#
#def multiply_by_five(x):
#    return x * 5
#
#print(double(multiply_by_five)(1))

#def call_twice(function, *args, **kwargs):
#    result1 = function(*args, **kwargs)
#    result2 = function(*args, **kwargs)
#    return (result1, result2)
#
#def filter_map(function, items):
#    result = []
#    for item in items:
#        if function(item)[0]:
#            result.append(function(item)[1])
#    return result

#def keep_truthful(items):
#    return filter(None, items)
#    
#def abs_sum(items):
#    if items:
#        return reduce(add, map(abs,(items)))
#    return 0
#    
#def abs_sum_1(numbers):
#    return sum(map(abs, numbers))
#
#
#def walk(tdict, path):
#    result = tdict.copy()
#    for i in range(len(path)):
#        result = (getitem(result, path[i]))
#    return result
#
#
#def walk_1(tdict, path):
#    return reduce(getitem, path, tdict)
#
#
#print( walk_1({'a': {7: {'b': 42}}}, ["a", 7, "b"]))

#printers = []
#for i in range(10):
#    def printer():
#        return i
#    printers.append(printer())


#printers = []
#for i in range(10):
#    def make_printer(arg):
#        def printer():
#            print(arg)
#        return printer
#    p = make_printer(i)
#    printers.append(p)
  
#def double(function):
#    def inner(argument):
#        return function(function(argument))
#    return inner
#
#def multiply_by_five(x):
#    return x * 5
#
#print(double(multiply_by_five)(3))



#def make_closure():
#
#    name = 'Alice'
#
#    def inner():
#        print('Hello', name)
#
#    return inner
#
#make_closure()()

#def greet(name, surname):
#    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
#
#
#def partial_apply(func, arg1):
#    def inner(arg2):
#        return func(arg1, arg2)
#    return inner
#
#def flip(func):
#    def inner(arg1, arg2):
#        return func(arg2,arg1)
#    return inner

#def make_module(step = 1):
#    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}

#def printing(function):
#    def inner(*args, **kwargs):
#        result = function(*args, **kwargs)
#        print('result =', result)
#        return result
#    return inner
#
#@printing
#def add_two(x):
#    return x + 2


#def memoized(func):
#    cache = {}
#    def inner(*args):
#        if args not in cache:
#            cache[args] = func(*args)
#        return cache[args]
#    return inner

#def memoized_1(function):
#    memory = {}
#
#    def inner(argument):
#        memoized_result = memory.get(argument)
#        if memoized_result is None:
#            memoized_result = function(argument)
#            memory[argument] = memoized_result
#        return memoized_result
#
#    return inner
#
#def memoizing(max_size):
#    def wrapper(function):
#        cache = {}
#        cache_order = []
#        #@wraps(function)
#        def inner(*args):
#            if args not in cache:
#                cache[args] = function(*args)
#                cache_order.append(args)
#                if len(cache) > max_size:
#                    cache.pop(cache_order.pop(0))
#            return cache[args]
#        return inner
#    return wrapper
#                    
#@memoizing(3)
#def add_six(x):
#    return x + 6
#
#def memoizing_1(limit):
#    """
#    Make decorator that will remember recent results of function (up to limit).
#
#    Arguments:
#        limit, maximum number of results to remember
#
#    Returns:
#        memoizing decorator
#
#    """
#    def wrapper(function):
#        """
#        Memoize function.
#
#        Arguments:
#            function, it will be memoized
#
#        Returns:
#            memoized version of function
#
#        """
#        memory = {}
#        order = []
#        @wraps(function)
#        def inner(argument):
#            memoized_result = memory.get(argument)
#            if memoized_result is None:
#                memoized_result = function(argument)
#                memory[argument] = memoized_result
#                order.append(argument)
#                if len(order) > limit:
#                    oldest_argument = order.pop(0)
#                    memory.pop(oldest_argument)
#            return memoized_result
#        return inner
#    return wrapper
#
#def cgego(func):
#    count = 1
#    res = []
#    def inner(arg):
#        res.append(arg)
#        return func(arg) + count
#
#    return inner
#
#@cgego
#def add_one(x):
#    return x + 1
#
#print(add_one(4))
#print(add_one(3))
#(count)
#@memoized
#def fibonacci(n):
#    if n <= 2:
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)
#fib_cache ={}
#def fibonacci_1(n):
#    if n in fib_cache:
#        return fib_cache[n]
#    if n <= 2:
#        value = 1
#    elif n > 2:
#        value = fibonacci_1(n-1) + fibonacci_1(n-2)
#    fib_cache[n] = value
#    return value
#
#print(fibonacci_1(1000))
#print(fib_cache)
#def is_even(n):
#    if n == 0:
#        return True
#    return is_odd(n-1)
#def is_odd(n):
#    if n == 0:
#        return False
#    return is_even(n-1)
#
#print(is_odd(7))
#print(is_even(8))

#def calculate_distance(point1, point2):
#    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#def make_decart_point(x, y):
#    return {'x':x, 'y' :y}
#
#def get_x(point):
#    return point["x"]
#
#def get_y(point):
#    return point["y"]
#
#def make_segment(point1, point2):
#    return {'start_point': point1, 'end_point': point2}
#
#def get_begin_point(segment):
#    return segment["begin_point"]
#
#
#def get_end_point(segment):
#    return segment["end_point"]
#
#
#def get_mid_point_of_segment(segment):
#    begin_point = get_begin_point(segment)
#    end_point = get_end_point(segment)
#
#    x = (get_x(begin_point) + get_x(end_point)) / 2
#    y = (get_y(begin_point) + get_y(end_point)) / 2
#
#    return make_decart_point(x, y)


#def make_decart_point_p(x, y):
#    return {
#        "angle": math.atan2(y, x),
#        "radius": math.sqrt((x ** 2) + (y ** 2)),
#    }
#
#def get_point_angle(point):
#    return point['angle']
#
#def get_point_radius(point):
#    return point['radius']
#
#def get_x_p(point):
#    return int(get_point_radius(point) * math.cos(get_point_angle(point)))
#
#def get_y_p(point):
#    return int(get_point_radius(point) * math.sin(get_point_angle(point)))

#def get_quadrant(point):
#    x = get_x(point)
#    y = get_y(point)
#
#    if x > 0 and y > 0:
#        return 1
#    if x < 0 < y:
#        return 2
#    if x < 0 and y < 0:
#        return 3
#    if y < 0 < x:
#        return 4
#
#    return None
#
#
#def make_rectangle(starting_point, width,height):
#    point1 = starting_point
#    point2 = make_decart_point(get_x(point1) + width, get_y(point1))
#    point3 = make_decart_point(get_x(point1) + width, get_y(point1) - height)
#    point4 = make_decart_point(get_x(point1), get_y(point1) - height)
#    return {'point1' : point1,
#            'point2' : point2,
#            'point3' : point3,
#            'point4' : point4
#            }
#
#def get_rectangle_point1(rectangle):
#    return rectangle['point1']
#
#def get_rectangle_point2(rectangle):
#    return rectangle['point2']
#
#def get_rectangle_point3(rectangle):
#    return rectangle['point3']
#
#def get_rectangle_point4(rectangle):
#    return rectangle['point4']
#
#
#def contains_origin(rectangle):
#    result = {get_quadrant(get_rectangle_point1(rectangle)),
#              get_quadrant(get_rectangle_point2(rectangle)),
#              get_quadrant(get_rectangle_point3(rectangle)),
#              get_quadrant(get_rectangle_point4(rectangle)),
#              }
#    if len(result) == 4:
#        return True
#    return False
                
    
#def make_rational(numer, denom):
#    norm_numer = int(numer / math.gcd(numer, denom))
#    norm_denom = int(denom / math.gcd(numer, denom))
#    return {'numer' : norm_numer, 'denom' : norm_denom}
#
#
#def rat_to_string(rat):
#    return "{}/{}".format(get_numer(rat), get_denom(rat))
#
#
#def get_numer(rational):
#    return rational['numer']
#
#def get_denom(rational):
#    return rational['denom']
#
#
#def add_rational(rational_1, rational_2):
#    if get_denom(rational_1) == get_denom(rational_2):
#        result = make_rational(get_numer(rational_1) + get_numer(rational_2), get_denom(rational_1))
#    else:
#        result = make_rational(get_numer(rational_1) * get_denom(rational_2) + get_numer(rational_2) * get_denom(rational_1), get_denom(rational_1) * get_denom(rational_2))
#    return result
#
#
#def sub_rational(rational_1, rational_2):
#    if get_denom(rational_1) == get_denom(rational_2):
#        result = make_rational(get_numer(rational_1) - get_numer(rational_2), get_denom(rational_1))
#    else:
#        result = make_rational(get_numer(rational_1) * get_denom(rational_2) - get_numer(rational_2) * get_denom(rational_1), get_denom(rational_1) * get_denom(rational_2))
#    return result
#
#def rgb(red, green, blue):
#    return red, green, blue
#
#class Color:
#    red = rgb(255, 0, 0)
#    green = rgb(0, 255, 0)
#    blue = rgb(0, 0, 255)
#    
#
#class RGB:  # noqa: WPS306
#    red = 0
#    green = 0
#    blue = 0
#
#
#red, blue, green = RGB(), RGB(), RGB()
#red.red = 255
#blue.blue = 255
#green.green = 255
#
#
#def rgb2tuple(rgb):
#    if isinstance(rgb, RGB):
#        return rgb.red, rgb.green, rgb.blue
    
    
#class Kounter:
#    def __init__(self, value=0):
#        self.value = value
#        
#    def inc(self, delta=1):
#        return Kounter(max(self.value + delta, 0))
#
#    def dec(self, delta=1):
#        return self.inc(-delta)
#    
#    
#class HourClock:
#    def __init__(self):
#        self.pos = 0
#        
#    @property
#    def hours(self):
#        return self.pos
#    
#    @hours.setter
#    def hours(self, delta):
#        self.pos = delta%12
        
#class Counter(object):
#    """A simple integral counter."""
#
#    def __init__(self):
#        """Initialize a new counter with zero as starting value."""
#        self.value = 0
#
#    def inc(self, amount=1):
#        """Increment counter's value."""
#        self.value = max(self.value + amount, 0)
#
#    def dec(self, amount=1):
#        """Decrement counter's value."""
#        self.inc(-amount)
#        
#class LimitedCounter(Counter):
#    def __init__(self, limit):
#        super().__init__()
#        self.limit = limit
#    
#    def inc(self, *args, **kwargs):
#        super().inc(*args, **kwargs)
#        self.value = min(self.value, self.limit)
#        
#  # Решение основано на замене атрибута value на свойство,
## setter которого ограничивает значение счётчика.
## Такой подход позволяет сохранить свойства класса даже
## если пользователь будет менять значение счётчика через
## присваивание напрямую атрибуту value.
##
## Если вы просто унаследуете Counter и переопределите
## метод inc, то такое решение тоже будет правильным.
## Данное решение нарочно демонстрирует альтернативный подход :)
#class LimitedCounter_1(Counter):
#    """A counter with limited maximal value."""
#
#    def __init__(self, limit):
#        """Initialize a new counter with some limit."""
#        self.limit = limit
#        # Свойство должно где-то хранить фактическое значение
#        # счётчика, для чего вводится "скрытый" ("приватный")
#        # атрибут _actual_value:
#        self._actual_value = 0
#        # Инициализация методом родителя делается в конце,
#        # потому что предок уже в __init__ присваивает атрибуту
#        # value значение 0. А это значит, что будет вызван setter,
#        # который использует атрибуты limit и _actual_value.
#        super().__init__()

#    @property
#    def value(self):
#        return self._actual_value
#
#    @value.setter
#    def value(self, new_value):
#        self._actual_value = min(max(new_value, 0), self.limit)
        

def suppress(exception, or_return=None):
    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                return or_return
        return inner
    return wrapper
