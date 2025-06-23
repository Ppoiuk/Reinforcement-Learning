class ParameterManager:
    @staticmethod
    def get_user_parameters(m, LCmin, UCmax, LD, UD, LP, UP, LN, UN, T):
        parameters = {
            "m": m,
            "LCmin": LCmin,
            "UCmax": UCmax,
            "LD": LD,
            "UD": UD,
            "LP": LP,
            "UP": UP,
            "LN": LN,
            "UN": UN,
            "T": T
        }
        return parameters
