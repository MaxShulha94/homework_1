def parse(query: str) -> dict:
    query_dict = {}

    if 'name' in query:
        query = (query.split('?')[1])
        if query:
            keys_values = query.split('&')
            for items in keys_values:
                if items == '':
                    keys_values.remove(items)
                else:
                    key, value = items.split('=')

                    query_dict[key] = value
            return query_dict
    else:
        return query_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    parse_dict = {}
    if query == '':
        return {}
    else:
        query = (query.split(';'))
        for items in query:
            if items == '':
                query.remove(items)
            else:
                symbol = items.find('=')
                key = items[:symbol]
                value = items.replace('=', ' ', 1).split(' ')[1]
                parse_dict[key] = value
        return parse_dict


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
