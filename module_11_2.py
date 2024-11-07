def introspection_info(obj):
    # Тип объекта
    type_name = type(obj).__name__

    # Атрибуты объекта
    attribute_list = dir(obj)

    # Методы объекта
    methods = [method for method in attribute_list if callable(getattr(obj, method))]

    # Модуль, к которому объект принадлежит
    module = obj.__class__.__module__

    # Другие интересные свойства объекта, учитывая его тип
    id_ = id(obj)
    symbol = chr(obj)

    # Создание словаря с информацией об объекте
    dict_info = {'type': type_name, 'attributes': attribute_list, 'methods': methods,
                 'module': module, 'id': id_, 'symbol': symbol}

    return dict_info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

