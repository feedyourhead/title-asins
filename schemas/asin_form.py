from formencode import Schema, validators


class AsinFormSchema(Schema):

    src_asin = validators.UnicodeString()
    src_site = validators.UnicodeString()
    dst_site = validators.UnicodeString()
