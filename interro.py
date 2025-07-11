import interro_requests as ir







def main():
    print("InterRobot initiated: enter question or 'quit' to exit:")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["quit","q","exit"]:
            print("Goodbye!")
            break

        parse_response = ir.parse_request(user_input)
        words = parse_response.split(",")
        if words[0] == "ON_TOPIC":
            response = ir.generate_on_topic(user_input)
        elif words[0] == "OFF_TOPIC":
            if words[1] == "jailbreak":
                response = ir.generate_off_topic_jailbreak(user_input)
            else:
                response = ir.generate_off_topic(user_input)
        elif words[0] == "ERROR!":
            response = ir.generate_error(words[1])



        tag = "</think>"
        before, sep, after = response.partition(tag)
        if sep: 
            response = after.lstrip()
        
            
            
        print(response)
            

if __name__=="__main__":
    main()