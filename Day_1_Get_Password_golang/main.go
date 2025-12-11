package main

import "fmt"

const session_cookie = "53616c7465645f5f257629c68340882a2f4c9317038ad7f407056d54347ba68f01d68f96295d4e2e01cedc40620aa58d796a708084a85ec680e433c996b3c924"
const year = 2025


func get_input_file(day int, session_cookie string){
	filename := fmt.Sprintf("input_day_%d.txt", day)
	fmt.Println(filename)
}

func main() {
    fmt.Println("Hello, World!")
	get_input_file(1, session_cookie)	
}
