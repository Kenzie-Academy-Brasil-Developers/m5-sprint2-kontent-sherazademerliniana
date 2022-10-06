class DataValidationError(Exception):
    ...

class ContentValidator: 
    valid_keys = [
        "title",
        "module",
        "students",
        "description",
        "is_active",
    ]

    valid_inputs = {
        "title": str,
        "module": str,
        "students": int,
        "description":str,
        "is_active": bool,
    }

    def __init__(self, *args: tuple, **kwargs: dict):
        self.data = kwargs
        self.errors = {}

    def is_valid(self):
        self.clean_data()
        
        try:
            self.validate_keys()
            self.validate_inputs()
            
            return True
        except (KeyError, DataValidationError):
            return False

    def clean_data(self):
        data_keys = list(self.data.keys())

        for key in data_keys:
            if key not in self.valid_keys:
                self.data.pop(key)

    
    def validate_keys(self):
        for valid_key in self.valid_keys:
            if valid_key not in self.data.keys():
                self.errors.update({valid_key: "missing key"})
        
        
        if self.errors:
            raise KeyError

    def validate_inputs(self):
        for valid_key, expected_type in self.valid_inputs.items():
            if type(self.data[valid_key]) is not expected_type:
                err_msg = f'must be a {expected_type.__name__}'
                self.errors[valid_key] = err_msg

        if self.errors:
            raise DataValidationError



        