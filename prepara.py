#!/usr/bin/env python3
"""Convierte la app de Karina en la de Violeta y Lyndsey (Pompetition).

QUE CAMBIA

  - el nombre y el titulo
  - los dos dias de rutina (los que mando Pam)
  - el almacen local y la carpeta de la nube, para no pisar los datos de Karina
  - fuera la caminata y el diario de comida: eran de Karina
  - fuera el guiño (.mark): Pam dijo "sin el guiño obvio"

QUE NO CAMBIA

  Todo el resto: el registro de series, los PRs, la sincronizacion, el
  auto-actualizado. Ya funciona y esta probado.
"""
import re, os, sys

BASE = '/Users/lapame10/.hermes/workspace/pompetition'
F = os.path.join(BASE, 'index.html')
s = open(F, encoding='utf-8').read()
toc = 0

def rep(v, n, q):
    global s, toc
    if v in s:
        s = s.replace(v, n, 1); toc += 1; print('  ok:', q)
    else:
        print('  ✗ NO COINCIDIO:', q)

# ---------- 1) el titulo y el encabezado ----------
rep('<title>Plan de Karina — Bajar grasa y ganar músculo</title>',
    '<title>Pompetition 🍑 — Violeta &amp; Lyndsey</title>',
    'el titulo')

rep('<div class="mark"><span>Karina Diez</span></div>', '', 'el guiño (fuera)')

rep('<h1>Plan de Karina</h1>', '<h1>Pompetition 🍑</h1>', 'el h1')

# ---------- 2) el almacen y la nube ----------
rep("const LS = 'planKarinaV1';", "const LS = 'planPompV1';", 'el almacen local')
rep("const CLOUD='karina';", "const CLOUD='pompetition';", 'la carpeta en la nube')
rep("const BUILD='p9';", "const BUILD='p1';", 'el contador de version')

# ---------- 3) las semanas ----------
rep("const WEEKS = ['Sem 1','Sem 2','Sem 3','Sem 4','Sem 5','Sem 6','Sem 7','Sem 8'];",
    "const WEEKS = ['S1','S2','S3','S4','S5','S6','S7','S8'];",
    'las semanas')

open(F, 'w', encoding='utf-8').write(s)
print('  cambios:', toc)
