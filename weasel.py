import random
import string

import click


VALID_CHARSET = string.ascii_uppercase + ' '


dxxef validate_target(ctx, param, value):
    if set(value).union(VALID_CHARSET) != set(VALID_CHARSET):
        raise click.BadParameter('Target string must only contain spaces and uppercase ASCII characters.')
    return value
