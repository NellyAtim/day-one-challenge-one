class Years:
    def get_year(self, input_year):
        try:
            year = int(input_year)
            this_year = 2019
            if year > 2019:
                print("Invalid year of birth")
                return "Invalid year of birth"
            else:
                our_results = this_year-year
                if our_results < 18:
                    print("You are a minor")
                    return "You are a minor"
                elif our_results>=18 and our_results<36:
                    print("You are a youth")
                    return "You are a youth"
                else:
                    print("You are an elder")
                    return "You are an elder"
        except:
            print("Not an integer")
            return "You must provide an integer"

test = Years()
test.get_year("1992")