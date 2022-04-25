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


class Api:
    def fetch_remote_data(self):
        print('Api Called')
        return 42

class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api return result: {api_result}')

from injector import Injector, Module, singleton, provider


class AppModule(Module):

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        return Api()

if __name__ == '__main__':
    injector = Injector(AppModule())
    logic = injector.get(BusinessLogic)
    logic.do_stuff()

class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api Called')
        return 24

class TestAppModule(Module):
    @singleton
    @provider
    def provider_api(self) -> Api:
        return TestApi()

if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()
     
