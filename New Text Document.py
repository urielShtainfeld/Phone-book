from phonebook import main as myscript_main

try:
    myscript_main()
except:
    print("Script errored!")
    print("Error message: %s")
    print("Traceback:")
    import traceback
    traceback.print_exc()
    print("Press return to exit..")
    input()
