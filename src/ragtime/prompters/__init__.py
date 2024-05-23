#!/usr/bin/env python3

from ragtime.base.prompter import *

from ragtime.prompters.answer.base import ( PptrAnsBase )
from ragtime.prompters.answer.with_retriever import ( PptrAnsWithRetrieverFR )
from ragtime.prompters.fact.fr import ( PptrFactsFR )
from ragtime.prompters.eval.fr import ( PptrEvalFR )

table:dict = {
    "PptrAnsBase": (lambda : PptrAnsBase()),
    "PptrFactsFR": (lambda: PptrFactsFR()),
    "PptrEvalFR": (lambda: PptrEvalFR()),
    "PptrAnsWithRetrieverFR": (lambda: PptrAnsWithRetrieverFR()),
}
