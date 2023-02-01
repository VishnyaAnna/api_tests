from voluptuous import Schema

create_user = Schema(
    {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    },
)

update_user = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str
    }
)

register_user = Schema(
    {
        'id': int,
        'token': str
    }
)


login_user = Schema(
    {
        'token': str
    }
)

unsuccessful_login_user = Schema(
    {
        'error': str
    }
)