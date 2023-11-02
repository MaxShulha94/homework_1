def parse(query: str) -> dict:
    query_dict = {}
    if '?' in query:
        query_params = query.split('?')[1].split('&')
        for param in query_params:
            if '=' in param:
                key, value = param.split('=')
                query_dict[key] = value
    return query_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    parse_dict = {}
    if query:
        pairs = query.split(';')
        for pair in pairs:
            key_value = pair.strip().split('=')
            if len(key_value) >= 2:
                key = key_value[0].strip()
                value = '='.join(key_value[1:]).strip()
                parse_dict[key] = value
    return parse_dict


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
