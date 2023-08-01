# Already used functions with outputs.
formatted_name = ['lkfjsdljk', 'fkdsk']
length = len(formatted_name)

# Return as an early exit
def format_name(f_name, l_name):
    a = "A String "
    """Take a first and last name and format it
    to return the title case version of the name."""
    # documentation string
    if f_name == "" or l_name == "":
        return "You didn't provide valid"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name}" \
           f"{formated_l_name}"
