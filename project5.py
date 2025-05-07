def shutdown(command):
    if command.lower() == "yes":
        return "Shutting down..."
    elif command.lower() == "no":
        return "Shutdown aborted!"
    else:
        return 
