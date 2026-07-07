# Function to print the field.
# Displays the selected value. Works for both player and AI fields.
def print_field(field,value):
    match value:
        case "ship":
            for row in field:
                print(" ".join([str(cell.ship) for cell in row]))
        case "ai_weight":
            for row in field:
                print(" ".join([str(cell.ai_weight) for cell in row]))
        case "render":
            for row in field:
                print(" ".join([str(cell.render) for cell in row]))
        case _:
            print("Invalid value. Please choose 'ship', 'ai_weight', or 'render'.")

