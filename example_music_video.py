import quantum_music
from quantum_music import make_music_video, get_instruments, chromatic_middle_c
import qiskit
from qiskit import QuantumCircuit

circ = QuantumCircuit(4)
circ.h(0)
circ.barrier()
circ.cx(0, 1)
circ.barrier()
circ.cx(1, 2)
circ.barrier()
circ.cx(2, 3)
circ.barrier()
circ.h(3)
circ.barrier()
circ.cx(3,2)
circ.barrier()
circ.cx(2,1)
circ.barrier()
circ.cx(1,0)
circ.barrier()

make_music_video(circ, "example_music_video", [(16, 8)]*8, 0.02, 0.05, [[57], get_instruments('tuned_perc')], note_map=chromatic_middle_c)