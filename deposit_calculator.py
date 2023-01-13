import argparse

def calculate_with_cap(...) -> float:
    ...

def calculate_without_cap(...) -> float:
    ...

def validate_init_sum(init_sum: float) -> None:
    if init_sum <= 0:
        raise Exception(f"Incorrect init sum. Must be greater than 0. You entered {init_sum}")

def format_output_message(result, init_sum,...) -> str:
    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("")
    init_sum = int(input())
    capitalization = True
    if capitalization:
        res = calculate_with_cap()
    else:
        res = calculate_without_cap()
    format_output_message(res, init_sum)
    init_sum = args.init_sum
    interest = args.interest





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
