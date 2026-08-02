#######################
# Sinmple Logging Lib #
#######################



# DESIGN TAGS:
# L -> Label
# X -> Name/Icon
# - -> White space
# <> -> Mini progress bar
# l -> Log level


class LogDesign():
    
    #RESET 
    RESET = "\033[0m"
    #GREEN
    COLOR1= "\033[32m"
    #YELLOW
    COLOR2 = "\033[33m"
    #RED
    COLOR3 = "\033[31m"




    template = "[L--X---]l"
    whitepace = " "
    iconChar = "i"

    logChar = whitepace
    warnChar = "W"
    errorChar = "E"

    logColor =  COLOR1
    warnColor = COLOR2
    errorColor = COLOR3


DSGN_BLKLIST = ["-","X","<",">","L"]
        

def log(logValue,logLevel=1,DesignObject=LogDesign,ShowLogLevel=False):
       out = ""
       for char in DesignObject.template:
           
           match char:
               case "L":
                   out += DesignObject.logChar
               case "l":
                   if ShowLogLevel: out += str(logLevel)
                   else:out += DesignObject.whitepace
               case "-":
                   out += DesignObject.whitepace
               case "X":
                   out += DesignObject.iconChar
               case _:
                   out += char

       out = DesignObject.logColor + out + DesignObject.RESET
       print(out , logValue)




def warn(warnValue,warnLevel=1,DesignObject=LogDesign,ShowWarnLevel=False):
    out = ""
    for char in DesignObject.template:
        
        match char:
            case "L":
                out += DesignObject.warnChar
            case "l":
                if ShowWarnLevel:out += str(warnLevel)
                else:out += DesignObject.whitepace
            case "-":
                out += DesignObject.whitepace
            case "X":
                out += DesignObject.iconChar
            case _:
                out += char


    out = DesignObject.warnColor + out + DesignObject.RESET
    print(out , warnValue)









def err(warnValue,DesignObject=LogDesign):
    out = ""
    for char in DesignObject.template:
        
        match char:
            case "L":
                out += DesignObject.errorChar
            case "l":
                out += DesignObject.whitepace
            case "-":
                out += DesignObject.whitepace
            case "X":
                out += DesignObject.iconChar
            case _:
                out += char


    out = DesignObject.errorColor + out + DesignObject.RESET
    print(out , warnValue)


