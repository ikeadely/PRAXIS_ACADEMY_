# A Quick Detour on Dependency Injection

# pip install injector
# Requirement already satisfied: injector in ./.local/lib/python3.8/site-packages (0.19.0)
# Requirement already satisfied: typing-extensions>=3.7.4; python_version < "3.9" in ./.local/lib/python3.8/site-packages (from injector) (4.2.0)

# class Api:
#     def fetch_remote_data(self):
#         print('Api called')
#         return 42

# class BusinessLogic:
#     def __init__(self, api: Api):
#         self.api = api

#     def do_stuff(self):
#         api_result = self.api.fetch_remote_data()
#         print(f'the api returned a result: {api_result}')

# if __name__ == '__main__':
#     api = Api()
#     lodic = BusinessLogic(api=api)

#     print(logic.do_stuff())

from msvcrt import getwch


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


# if __name__ == '__main__':
#     injector = injector(AppModule())

#     logic = injector.get(BusinessLogic)
#     logic.do_stuff()

class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api called')
        return 24

# if __name__ == '__main__':
#     real_injector = Injector(AppModule())
#     test_injector = Injector([AppModule(), TestAppModule()])

#     real_logic = real_injector.get(BusinessLogic)
#     real_logic.do_stuff()

#     test_logic = test_injector.get(BusinessLogic)
#     test_logic.do_stuff()

# 
# ^^ gtw