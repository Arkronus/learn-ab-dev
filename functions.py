def _set_qid_and_current_question(qid, questions):
    if qid and qid.isdigit():
        qid = int(qid)
    else:
        qid = 1

    if qid > len(questions):
        qid = len(questions)

    if questions:
        current_question = questions[qid - 1]
    else:
        current_question = None
    return qid, current_question


def _set_is_final(isf):
    print(isf)
    if isf:
        print('if')
        print(isf.lower)
        return isf.lower() == 'true'
    else:
        return False
