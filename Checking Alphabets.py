print ( "\033c" )

character = input ( "enter a character : " )

if character >= "a" and character <= "z" :
    print ( f"\n{ character } is a lowercase alphabet" )

elif character >= "A" and character <= "Z" :
    print ( f"\n{ character } is a uppercase alphabet" )

else :
    print ( f"\n{ character } is not an alphabet" )