# Create class RouteFactory - with implementation of the factory for generating different URL which
#    depends of the user input
import os


class RelativeRoute:
    # type of Object to return
    def __init__(self, route):
        self.route = os.path.dirname(os.path.realpath(__file__)) + "\\" + route
    # method to represent object
    def __str__(self):
        return self.route


class AbsoluteRoute:
    # type of Object to return
    def __init__(self, route):
        self.route = f"http://www.{route}.com"
    # method to represent object
    def __str__(self):
        return self.route


class RouteFactory:
    # factory method to retrieve and add easily different type of routes
    def get_route(self, route_type="Absolute", route=""):
        routes = dict(
            Absolute=AbsoluteRoute(route),
            Relative=RelativeRoute(route))
        return routes[route_type]


factory = RouteFactory()

print(factory.get_route("Absolute", "google"))
