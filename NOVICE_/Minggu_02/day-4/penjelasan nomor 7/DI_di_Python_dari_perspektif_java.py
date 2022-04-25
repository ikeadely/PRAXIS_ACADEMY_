# A Quick Detour on Dependency Injection


from sys import api_version

class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42

class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')

if __name__ == '__main__':
    api = Api()
    logic = BusinessLogic(api=api)

    print(logic.do_stuff())

# pip install injector
# Requirement already satisfied: injector in ./.local/lib/python3.8/site-packages (0.19.0)
# Requirement already satisfied: typing-extensions>=3.7.4; python_version < "3.9" in ./.local/lib/python3.8/site-packages (from injector) (4.2.0)

# from injector import Module


# class Api:
#     def fetch_remote_data(self):
#         print('Api Called')
#         return 42

# class Businesslogic:
#     def __init__(self, api: Api):
#         self.api = api

#     def do_stuff(self):
#         api_result = self.api.fetch_remote_data()
#         print(f'the api return result: {api_result}')

# class AppModule(Module):

#     @singleton
#     @provider
#     def provide_business_logic(self, api: Api) -> BusinessLogic:
#         return BusinessLogic(api=api)

#     @singleton
#     @provider
#     def provide_api(self) -> Api:
#         configuration
#         return Api()

# if __name__ == '__main__':
#     injector = injector(AppModule())
#     logic = injector.get(Businesslogic)
#     logic.do_stuff()

class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api Called')
        return 24
