import json
import os
import pandas


def filter_data(data):
    # CONVERT TO PROMPT/RESPONSE FORMAT
    convo_list = []

    for row in data.iterrows():
        for i in range(1, 10):
            prompt = row[1]["Answer.sentence" + str(i)]
            response = row[1]["Answer.sentence" + str(i + 1)]
            convo_list.append({"prompt": prompt, "response": response})

    return convo_list


if __name__ == "__main__":
    print("File loaded")
    basepath = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(
        basepath,
        "../data/Batch_2840986_batch_results.csv",
    )
    data_csv = pandas.read_csv(filepath)

    print("Processing data")
    data = filter_data(data_csv)

    file = open(os.path.join(basepath, "../data/data.json"), "w")
    file.write(json.dumps(data, indent=2))
    file.close()
    print("File written to data/data.json")
