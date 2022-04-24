# A Quick Detour on Dependency Injection

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
    lodic = BusinessLogic(api=api)

    print(logic.do_stuff())

class AppModule(Module):

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        # there is no complex logic in our case,
        # but you can use this method to hide the complexity of initial 
        configuration
        # e.g. when instantiating a particular DB connector.
        return Api()
