import main as main

## Requirement 6 : Given a list, get the user data and return a map with user input details
def t_get_user_input_for_list_external_dep():
    input_list = ["<<<TO_NAME>>>", "<<<BOOK_NAME>>>"]
    result = {"<<<TO_NAME>>>": "Spandana", "<<<BOOK_NAME>>>": "Outliers"}
    filIO = main.FileIO()
    if(result != filIO.get_user_input_for_list_external_dep(input_list)):
        print("Test Fail : test_get_user_input_for_list_external_dep")
    else:
        print("Success")

t_get_user_input_for_list_external_dep()