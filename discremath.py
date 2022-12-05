#!/usr/bin/env python3
# -*- coding; utf-8 -*-

import sys
import os
from subprocess import call

arquivo, extensao = os.path.splitext(sys.argv[1])
if extensao != ".dmath":
    raise Exception("Arquivo com extensao invalida! Somente aceito .dmath")

call("python " + "sintatica.py " + f"{arquivo}{extensao}", shell=True)

isempty = os.stat(f"erros_{arquivo}.txt").st_size == 0

if(isempty):
    call("python " + f"{arquivo}.py", shell=True)
