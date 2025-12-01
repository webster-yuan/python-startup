
class ApiRouter:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorate(func):
            self.routes[path] = func
            return func
        return decorate

router = ApiRouter()

@router.route("/home")
def home():
    return "Welcome to Home Page"

@router.route("/about")
def about():
    return "About Us"

if __name__ == '__main__':
    print(router.routes)

# {'/home': <function home at 0x0000022C7EE939C0>, '/about': <function about at 0x0000022C7EE93A60>}