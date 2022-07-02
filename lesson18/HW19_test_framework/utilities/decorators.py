import inspect
import allure

class HelperDecorators:

    @staticmethod
    def auto_steps(cls):
        for fn_name, funk in inspect.getmembers(cls):
            if (not inspect.isfunction(funk)) or inspect.isbuiltin(funk) and funk.name.startswith("__"):
                continue
            setattr(cls, fn_name, allure.step(funk))
        return cls