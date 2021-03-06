import quantum_music
from quantum_music import make_music_midi, make_music_video, get_instruments, chromatic_middle_c
import qiskit
from qiskit import QuantumCircuit

repeats = 8

circ = QuantumCircuit(5)
circ.x(0)
circ.x(1)
circ.x(2)
circ.h(4)
circ.cx(4,2)
i = 0
while i < repeats:
    i += 1
    circ.barrier()
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,1)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.x(1)
    circ.cx(4,3)
    circ.cx(4,1)
    circ.cx(4,0)
    circ.barrier()
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,1)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.x(0)
    circ.cx(4,3)
    circ.cx(4,0)
    circ.barrier()
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,1)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.x(0)
    circ.x(1)
    circ.x(2)
    circ.cx(3,4)
    circ.barrier()
    circ.barrier()
    circ.cx(3,4)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,0)
    circ.x(1)
    circ.x(2)
    circ.cx(4,2)
    circ.barrier()
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,2)
    circ.cx(4,0)
    circ.barrier()
    circ.cx(4,3)
    circ.cx(4,2)
    circ.cx(4,1)
    circ.barrier()
    if i != repeats:
        circ.x(1)
        circ.cx(4,3)
        circ.cx(4,0)


time_list = [(60,0),(60,0),(60,60),(60,120),(60,60),(60,60),(120,0),(60,0),(60,0),(60,0)]*4*repeats
chromatic_G1 = lambda n: n + 31

make_music_video(circ, "megalovania_loop", time_list, 0.01, 0.02, [[81],[80]], note_map=chromatic_G1, circuit_layers_per_line=80)
#make_music_video(circ, "megalovania_loop", time_list, 0.01, 0.02, [[81],[80]], note_map=chromatic_G1)