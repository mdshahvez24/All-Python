def mutuate_string(string, position, character):
    string = "abracadabra"
    return string[:position]+character+string[position+1:]
mutuate_string()