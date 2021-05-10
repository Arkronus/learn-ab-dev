from flask import Markup


def _set_qid_and_current_question(qid, questions):
    if qid and qid.isdigit():
        qid = int(qid)
    else:
        qid = 1

    if qid > len(questions):
        qid = len(questions)

    if questions:
        current_question = questions[qid - 1]
        current_question.text = Markup(current_question.text)
    else:
        current_question = None
    return qid, current_question


