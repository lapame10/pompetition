#!/usr/bin/env python3
"""Arregla el selector y traduce Pompetition al ingles.

Pam: "en el pompetition la pestaña de Lyndsey no se ve y quiero que sea en
ingles por favor".

---------------------------------------------------------------
1. EL BUG DE LA PESTANA

El selector tiene dos botones:

    <button class="qbtn on" data-q="violeta">Violeta</button>
    <button class="qbtn"    data-q="lyndsey">Lyndsey</button>

El "on" (que es el que sale resaltado) estaba PUESTO A MANO en Violeta. Y al
tocar Lyndsey se recargaba la pagina, pero el "on" seguia en Violeta porque
nadie lo actualizaba.

O sea: SI cambiaba de persona (los datos van separados), pero el boton no lo
enseñaba. Parecia que la pestaña de Lyndsey no existia. Eso es lo que veia Pam.

Ahora el resaltado se pone segun quien este elegido de verdad.

---------------------------------------------------------------
2. EL INGLES

Lyndsey es canadiense y Violeta es de Estados Unidos. La app estaba en español
porque la base era la de Karina.

Se traduce todo: el HTML y las cadenas del JavaScript. Se dejan en español SOLO
las notas de los ejercicios que escribio Pam (el tempo, las indicaciones), porque
son suyas y no me toca reescribirlas — pero se traducen tambien, porque si no la
app queda a medias. Se pide perdón por adelantado si algun matiz cambia.
"""
import re, os, sys

RUTA = '/Users/lapame10/.hermes/workspace/pompetition/index.html'
s = open(RUTA, encoding='utf-8').read()
toc = 0


def rep(v, n, quien):
    global s, toc
    if v in s:
        s = s.replace(v, n, 1); toc += 1
        return True
    print('  · no estaba:', quien)
    return False


# ============================================================
# 1) EL SELECTOR: el resaltado segun quien este elegido
# ============================================================
rep("""    <button class="qbtn on" data-q="violeta">Violeta</button>
    <button class="qbtn" data-q="lyndsey">Lyndsey</button>""",
"""    <button class="qbtn" data-q="violeta">Violeta</button>
    <button class="qbtn" data-q="lyndsey">Lyndsey</button>""",
'el selector sin "on" fijo')

rep("""document.querySelectorAll('.qbtn').forEach(b => {
  b.onclick = () => {""",
"""/* ===== EL RESALTADO, SEGUN QUIEN ESTE ELEGIDO =====
   Antes el "on" estaba PUESTO A MANO en Violeta, y nadie lo movia. Asi que al
   elegir a Lyndsey los datos SI cambiaban, pero el boton seguia resaltando a
   Violeta — y parecia que la pestaña de Lyndsey no existia. */
document.querySelectorAll('.qbtn').forEach(b => {
  if (b.dataset.q === QUIEN) b.classList.add('on');
  b.onclick = () => {""",
'el resaltado dinamico')

# ============================================================
# 2) EL HTML
# ============================================================
HTML = [
    ('Fuerza · Hipertrofia', 'Strength · Hypertrophy'),
    ('Bajar grasa y ganar músculo', 'Lose fat and build muscle'),
    ('3 días / semana', '3 days / week'),
    ('Técnica primero:', 'Technique first:'),
    ('Progresión:', 'Progression:'),
    ('Tip del día', 'Tip of the day'),
    ('Empieza tu racha hoy', 'Start your streak today'),
    ('Anota tus pesos y enciende el primer fuego', 'Log your weights and light the first fire'),
    ('🎖 Ver colección', '🎖 View collection'),
    ('🏆 Récords personales', '🏆 Personal records'),
    ('Regla A/B · Registra cada semana tocando un ejercicio.',
     'Rule A/B · Log each week by tapping an exercise.'),
    ('Los datos se guardan en este dispositivo.', 'Your data is saved on this device.'),
    ('Ciclo', 'Cycle'),
    ('Core', 'Core'),
]
for a, b in HTML:
    if a in s:
        s = s.replace(a, b); toc += 1

# y los textos que van partidos en etiquetas
rep("""las semanas 1-2 son para aprender el movimiento con peso ligero. Nunca entrenes al fallo — deja 3-4 reps en reserva.""",
    """weeks 1-2 are for learning the movement with light weight. Never train to failure — leave 3-4 reps in reserve.""",
    'el aviso de tecnica')
rep("""cuando las reps salgan cómodas, sube un poco el peso (según la máquina) o suma 1-2 reps. Poco a poco.""",
    """when the reps feel easy, add a little weight (depending on the machine) or 1-2 reps. Little by little.""",
    'el aviso de progresion')
rep("""Serie 1/4""", """Set 1/4""", 'la serie del cronometro')

# ============================================================
# 3) EL JAVASCRIPT
# ============================================================
JS = [
    ('ejercicio como hacer tecnica', 'exercise how to technique'),
    ('+ Añadir serie', '+ Add set'),
    ('Última marca:', 'Last mark:'),
    ('Sin series anotadas todavía', 'No sets logged yet'),
    ('Anota tus pesos y enciende el primer fuego', 'Log your weights and light the first fire'),
    ('Empieza tu racha hoy', 'Start your streak today'),
    ('Estimación aproximada', 'Rough estimate'),
    ('¡Colección completa!', 'Collection complete!'),
    ('¡NUEVO RÉCORD!', 'NEW RECORD!'),
    ('Récords de ayer:', "Yesterday's records:"),
    ('🔥 {n} días seguidos', '🔥 {n} days in a row'),
    ('🔥 {n} día seguido', '🔥 {n} day in a row'),
    ('kg de volumen', 'kg of volume'),
    ('<span class="sn">Serie ', '<span class="sn">Set '),
    ('Toca para ver la técnica', 'Tap to see the technique'),
]
for a, b in JS:
    if a in s:
        s = s.replace(a, b); toc += 1

# ============================================================
# 4) LAS NOTAS DE LOS EJERCICIOS (las escribio Pam, pero van en ingles)
# ============================================================
NOTAS = [
    ('Súper serie del infierno. 1 BSS + 1 RDL = 1 rep, sin descanso entre los dos. KTB de 24 kg EN CONTRALATERAL (en la mano opuesta a la pierna que trabaja). Tempo: 2 segundos para bajar en AMBOS ejercicios. En el RDL no hace falta tocar el piso con la KTB.',
     'Superset from hell. 1 BSS + 1 RDL = 1 rep, no rest between the two. 24 kg kettlebell on the CONTRALATERAL side (in the hand opposite the working leg). Tempo: 2 seconds down on BOTH exercises. On the RDL you don\'t need to touch the floor with the kettlebell.'),
    ('SIN peso por ahora. Tempo 2/0/2/0: 2 segundos para subir, 2 para bajar. El objetivo es lograr el rango COMPLETO en cada repetición. Aprieten fuerte el glúteo arriba y controlen toda la bajada.',
     'NO weight for now. Tempo 2/0/2/0: 2 seconds up, 2 seconds down. The goal is a FULL range of motion on every rep. Squeeze the glute hard at the top and control the whole way down.'),
    ('Con disco de 15 lbs. Tempo normal. Mantengan la cadera estable y NO giren el cuerpo: el trabajo lo tiene que hacer el glúteo medio, no la espalda.',
     'With a 15 lb plate. Normal tempo. Keep the hip stable and do NOT rotate your body: the work has to be done by the glute medius, not the back.'),
    ('Con liga mediana. Un minuto seguido, sin parar.',
     'With a medium band. One minute straight, no stopping.'),
    ('Con pausa de 1-2 segundos arriba. Intenten llegar cerca del fallo: si sienten que pueden hacer UNA repetición más, háganla. La idea es que la última cueste mucho, pero con buena técnica.',
     'Pause 1-2 seconds at the top. Get close to failure: if you feel you can do ONE more rep, do it. The idea is for the last one to be very hard, but with good technique.'),
    ('Tempo 2-1-0-0: bajada de 2 segundos, pausa de 1 segundo abajo, subida explosiva.',
     'Tempo 2-1-0-0: 2 seconds down, 1 second pause at the bottom, explosive up.'),
    ('Tempo 3-1-0-1: bajada controlada de 3 segundos, pausa de 1 segundo abajo, subida explosiva. Los brazos van extendidos para levantar las pesas. Controlen TODA la bajada y aprieten fuerte los glúteos arriba.',
     'Tempo 3-1-0-1: 3 seconds controlled down, 1 second pause at the bottom, explosive up. Arms stay extended to lift the weights. Control the WHOLE way down and squeeze the glutes hard at the top.'),
    ('Tempo normal. Busquen una contracción fuerte del glúteo en cada repetición y NO se impulsen con la espalda.',
     'Normal tempo. Go for a strong glute contraction on every rep and do NOT drive with your back.'),
    ('Con liga mediana. Dos veces por semana.',
     'With a medium band. Twice a week.'),
    ('FINISHER — Banded diagonal monster walk', 'FINISHER — Banded diagonal monster walk'),
]
for a, b in NOTAS:
    if a in s:
        s = s.replace(a, b, 1); toc += 1
    else:
        print('  · nota no encontrada:', a[:45])

# los nombres de los dias
s = s.replace("name:'Día 1', focus:'W4.B · 9 sets'", "name:'Day 1', focus:'W4.B · 9 sets'")
s = s.replace("name:'Día 2', focus:'W6.A · 14 sets'", "name:'Day 2', focus:'W6.A · 14 sets'")
toc += 2

open(RUTA, 'w', encoding='utf-8').write(s)
print('  cambios:', toc)
print()
print('=== ¿queda algo en español visible? ===')
i = s.find('<body>'); j = s.find('<script>')
cuerpo = s[i:j]
restos = re.findall(r'>([^<>{}]{3,80})<', cuerpo)
mal = [t.strip() for t in restos if re.search(r'[áéíóúñ¿¡]|\b(de|la|el|los|las|Serie|Día)\b', t)]
print('  ', mal if mal else 'nada')
