import os
import file_manager as fm
import system_design as sd

def newscript(inp):

    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) == 0 or inp[0] == '':
        sd.err('CSE', 'CommandStructure', 'Requires 1 argument: script name.')
        return
    else:
        with open(f'C:/TerminalBasic/scripts/{inp[0]}', 'w'):
            pass
        sd.msg('CSE', 'success', f"New script '{inp[0]}' successfuly created.")

def scriptlist(inp):

    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) != 0:
        sd.err('CSE', 'CommandStructure', 'Command requires no arguments.')
    else:
        sd.sysoutb()
        print('Scripts avaible for execution:')
        for i in os.listdir('C:/TerminalBasic/scripts'):
            print(f'\n{i}')
        sd.sysoute()


def cseReadInput(inp):

    command = ''

    for i in range(len(inp)):
        if inp[i] != ' ':
            command += inp[i]
        else:
            break

    if command == 'commandlist':
        sd.csecommandlist()
    elif command == 'newscript':
        newscript(inp)
    elif command == 'scriptlist':
        scriptlist(inp)
    elif command == '':
        return
    elif command == 'chmodule':
        var = fm.wrapper(fm.menu)
        if var == 'Menu abandoned, no dicision made.':
            sd.msg(fm.terminal_state, 'warning', var)
        else:
            fm.terminal_state = var
    elif command == '':
        return
    elif command == 'clear':
        os.system('cls')
        print()
    else:
        sd.err(fm.state,'CommandStructure', f"'{command}' is not recognized as a command.")