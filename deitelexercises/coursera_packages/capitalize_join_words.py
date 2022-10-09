def capitalize_join_words(sentence):
    if sentence.startswith('*'):
        s = sentence.replace('*', '')
        s2 = s.split()

        s3 = []
        for word in s2:
            s3 += word.capitalize()
        temp = ",".join(s3)
        sentence_revised = temp
    else:
        s = sentence.split()
        sentence_revised = ",".join(s)

    return sentence_revised