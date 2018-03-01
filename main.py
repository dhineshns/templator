def replace_string(template, string_to_be_replaced, replacing_string):
    return template.replace(string_to_be_replaced, replacing_string)

def gen_text_from_template(template, replaced_to_replacing_map):
    for replaced, replacing in replaced_to_replacing_map.iteritems():
        template = replace_string(template, replaced, replacing)
    return template

