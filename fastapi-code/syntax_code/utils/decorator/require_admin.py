from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role, *args):
        if user_role != "admin":
            raise PermissionError("Only admin can access this function!")
        return func(user_role)

    return wrapper


@require_admin
def delete_database(user_role):
    print("Database deleted!")


if __name__ == '__main__':
    delete_database("admin")
    delete_database("user")

# Traceback (most recent call last):
#   File "G:\startup\fastapi-code\syntax_code\utils\decorator\require_admin.py", line 19, in <module>
#     delete_database("user")
#     ~~~~~~~~~~~~~~~^^^^^^^^
#   File "G:\startup\fastapi-code\syntax_code\utils\decorator\require_admin.py", line 8, in wrapper
#     raise PermissionError("Only admin can access this function!")
# PermissionError: Only admin can access this function!

# Database deleted!
