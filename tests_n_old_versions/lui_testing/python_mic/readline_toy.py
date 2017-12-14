import readline

cmd_lst = [
          'import',
          'find_spots',
          'index',
          'refine_bravais_settings',
          'reindex',
          'refine',
          'integrate',
          'export',
          'exit',
          ]

def completer(text, state):
    options = [x for x in cmd_lst if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

if(__name__ == "__main__"):
    command = ""
    while( command.strip() != 'exit' and command.strip() != 'quit' ):
        command = str(raw_input("[[dials.>> "))
        print "You entered:", command

