##Question
# You had been a lackadaisical teenager. In conversation,
# your responses were very limited. You answered 'Sure.' 
# if asked a question, such as "How are you?". You 
# answered 'Whoa, chill out!' if somebody YELLED AT YOU 
# (in all capitals).You answered 'Calm down, I know what 
# I'm doing!' if a question was yelled at you. You would 
# say 'Fine. Be that way!' if addressed without actually 
# saying anything. You answered 'Whatever.' to anything else.

# Now that you have finished that phase of yours and 
# are “Python Geek” in making, you want to write a 
# script “MyTeenageResponses”, to mimic the lackadaisical 
# teenager, you were!.

# Following are few testcases for you to implement
# Input => "WATCH OUT!" ,Output=>"Whoa, chill out!"
# Input => ""You are, what, like 16?",Output => "Sure."
# Input => ""Hi there!"),Output =>" "Whatever.”
# Input => "WHAT'S GOING ON?" ,Output =>"Calm down, I know what I'm doing!"
# Input => " " Output =>"Fine. Be that way!"

##Answer
while True:
    message = ""+input("You:")
    if '?' in message and message.isupper():
        print("Bot: Calm down, I know what I'm doing!")
    elif message.isupper():
        print("Bot: Whoa, chill out!")
    elif '?' in message:
        print("Bot: Sure.")
    elif ""==message.strip():
        print("Bot: Fine. Be that way!")
    else:
        print("Bot: Whatever.")
        
