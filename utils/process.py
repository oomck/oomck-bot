def filter_data(itr):
    # CONVERT TO PROMPT/RESPONSE FORMAT
    convo_list = []
    cur_id = ""
    cur_speaker = ""
    prompt = ""
    response = ""
    speaking = 0

    for i, row in itr:
        # Initialize first convo
        if i == 0:
            cur_id = row["dialogueID"]
            cur_speaker = row["from"]

        if cur_id == row["dialogueID"]:
            if not cur_speaker == row["from"]:
                # If currently gathering sender text, switch
                if speaking == 0:
                    speaking = 1
                    response = str(row["text"]) + " "
                    cur_speaker = row["from"]
                # If currently gathering responders text, push to convo list and swap
                else:
                    cur_speaker = row["from"]
                    convo_list.append({"prompt": prompt, "response": response})
                    prompt = response
                    response = str(row["text"]) + " "
            elif speaking == 0:
                prompt += str(row["text"]) + " "
            else:
                response += str(row["text"]) + " "
        else:
            if not response == "":
                convo_list.append({"prompt": prompt, "response": response})
            speaking = 0
            cur_id = row["dialogueID"]
            cur_speaker = row["from"]
            prompt = str(row["text"]) + " "
            response = ""

    return convo_list
