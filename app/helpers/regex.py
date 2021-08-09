def build_regex(name, level='DEBUG|INFO|WARNING|ERROR|CRITICAL', y='[0-9]{4}', m='[0-1][0-9]', d='[0-3][0-9]',
                h='[0-1][0-9]|[2][0-3]', mi='[0-5][0-9]', s='[0-5][0-9]', ms='[0-9]{3}'):
    expression = '('
    expression += y
    expression += ')-('
    expression += m
    expression += ')-('
    expression += d
    expression += ').('
    expression += h
    expression += '):('
    expression += mi
    expression += '):('
    expression += s
    expression += '),('
    expression += ms
    expression += ').-.('
    expression += name
    expression += ').-.('
    expression += level
    expression += ')'
    return expression
