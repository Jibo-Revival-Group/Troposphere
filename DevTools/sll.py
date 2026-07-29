#######################
# Sinmple Logging Lib #
#######################



# DESIGN TAGS:
# L -> Label
# X -> Name/Icon
# - -> White space
# <> -> Mini progress bar
# l -> Log level

DSGN_BLKLIST = ["-","X","<",">","L"]


LOGGING_WHITESPACE = " "
LOGGING_TAG = ""
LOGGING_TEMPLATE = "[L--X---]l"

DESIGN_LOG = ""


def log_design_setup(tag=LOGGING_TAG, design=LOGGING_TEMPLATE, clr=LOGGING_WHITESPACE):
    out=""
    for char in design:
        if char in DSGN_BLKLIST :
            match char:
                case "X":
                    out += tag 
                case _:
                    out += clr
        else:
            out += char
    return out
    

        

def log(logValue,logLevel=1):
    out = ""
    for char in DESIGN_LOG:
        if char == "L":
            out += LOGGING_WHITESPACE
        elif char == "l":
            out += str(logLevel)
        else:
            out += char

    print(out , logValue)



DESIGN_LOG = log_design_setup()
log("testing!")











