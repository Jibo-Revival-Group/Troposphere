#!/bin/sh



echo "Troposphere for Jibo megascript!, setting colors"

RE_SET="\033[0m"
BOLD="\033[1m"

# Foreground Colors
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"

# Background Colors
BG_RED="\033[41m"
BG_GREEN="\033[42m"

# Clear the screen

clear

printf "${YELLOW} YAY ${RED}CO${GREEN}LO${BLUE}RS!"
# ------------------ [FUNCTIONS]
center_text() {
    # Get the number of columns in the terminal (defaults to 80 if it fails)
    cols=$(stty size 2>/dev/null | cut -d' ' -f2)
    : "${cols:=80}"
#   echo $cols 
    text="$1"
    
    # Calculate padding space
    # (Terminal Width - Text Length) / 2
    padding=$(( (cols - ${#text}) / 2 )) 
    
    # Print the padding spaces, then the text
    printf "%${padding}s%s\n" "" "$text"
}


center_text "Centered!"

center_text "                                              "
center_text "           ~@@@@@@@@@@@@@@@@@@@@-             "
center_text "        :@@@@@@@@@@@@@@@@@@@@@@@@@@:          "
center_text "      .@@@@@@@@)~..::.    >([@@@@@@@@.        "
center_text "     >@@@@@@(~     ...    =))*~(@@@@@@=       "
center_text "    <@@@@@=*+:     ..      :-::--)@@@@@}      "
center_text "   ~@@@@}         .^@@@@@+  .:--:-~]@@@@(     "
center_text "  .@@@@^         {@@@@@@@@@< :::::-->@@@@=    "
center_text "  ]@@@]         }@@@@@@@@@@@=::..:---]@@@@    "
center_text " .@@@@.         @@@@@<~%@@@@#:::::---=@@@@    "
center_text " ~@@@@          @@@@@@@@@@@@@::-:::--~]@@@    "
center_text " =@@@@:         @@@@@@@@@@@@).::::::-~@@@@    "
center_text " ~@@@@@         .@@@@@@@@@@@ ..::.:::*@@@@    "
center_text " .@@@@@%          *@@@@@@@+   ......=@@@@@    "
center_text "  ]@@@@@@:                    ....:+@@@@@^    "
center_text "  :@@@@@@@]                  ...:=@@@@@@#.    "
center_text "   =@@@@@@@@@~               .~^@@@@@@@@=     "
center_text "    ~%@@@@@@@@@@^~.       .*(@@@@@@@@@(+      "
center_text "     -]@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-)]=      "
center_text "       +[{[){@@@@@@@@@@@@@@@@@@@@#*-^[}=      "
center_text "       :~=>]%{%@@@@@@@@@@@@[{<:=<}+:}%^       "
center_text "       :.-^@@><[[]<*===~-:...-~~=().{@=       "
center_text "       :-+@@(-++~:.       .:~---:^(-=@}       "
center_text "        -@@%-=+=-.       .:-~--::=<^ [@=      "
center_text "       .@@@--+~:.      .::-----:-~*>.=@]      "
center_text "     =^%@@-.=~:    .::----::-----~=^~ {%:     "
center_text "    .+:@@}~:~~-~~~~~~~~-----~~~--~~++ )@=     "
center_text "     =<@@}==>>+:*<>*==~~~~~~~~~-~~~=+ ^%*     "
center_text "      @@@@*++:-*^~++*>)]]>+++++==+*^+.^#+     "
center_text "      @@*@){@@@{(>({#%@%%#}[()>=.:=-^{@@>:    "
center_text "      @@^@~+)]}}{{{#%#}(([#{[(()<* (@@@#^-    "
center_text "      }@@@@[~.:----:..  ..:-~--~=={@%@@@^:    "
center_text "     .^@@@@@@@@@@@@@@@@%#{[[[{@@@@@@@@@~      "
center_text "     .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=      "
center_text "      ~*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@{+-      "
center_text "       .<@@@@@@@@@@@@@@@@@@@@@@@@@@@@-        "
center_text "         -@@@@@@@@@@@@@@@@@@@@@@@@@[.         "
center_text "                                              "


echo ""
echo ""
echo ""


printf "${YELLOW} WELCOME TO TROPOSPHERE BOOTLOADER!"









