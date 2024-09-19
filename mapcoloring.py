from ortools.sat.python import cp_model

# Instantiate model and solver
model = cp_model.CpModel()
solver = cp_model.CpSolver()

freqs = {0: 'f1', 1: 'f2', 2: 'f3'}

# ## colors: 0: Red, 1: Blue 2: Green
# colors = {0 : 'Red',1:'Blue',2:'Green'}

# SF = model.NewIntVar(0,2,'SF')
# Alameda = model.NewIntVar(0,2,'Alameda')
# Marin = model.NewIntVar(0,2,'Marin')
# SanMateo = model.NewIntVar(0,2,'San Mateo')
# SantaClara = model.NewIntVar(0,2,'Santa Clara')
# ContraCosta = model.NewIntVar(0,2,'Contra Costa')
# Solano = model.NewIntVar(0,2,'Solano')
# Napa = model.NewIntVar(0,2,'Napa')
# Sonoma = model.NewIntVar(0,2,'Sonoma')

# Antenna1 = model.NewIntVar(0,2, "A1")

# ## add edges
# model.Add(SF != Alameda)
# model.Add(SF != Marin)
# model.Add(SF != SanMateo)
# model.Add(ContraCosta != Alameda)
# model.Add(Alameda != SanMateo)
# model.Add(Alameda != SantaClara)
# model.Add(SantaClara != SanMateo)
# model.Add(Marin != Sonoma)
# model.Add(Sonoma != Napa)
# model.Add(Napa != Solano)
# model.Add(Solano != ContraCosta)
# model.Add(ContraCosta != Marin)

A1 = model.NewIntVar(0, 2, "Num1")
A2 = model.NewIntVar(0, 2, "Num2")
A3 = model.NewIntVar(0, 2, "Num3")
A4 = model.NewIntVar(0, 2, "Num4")
A5 = model.NewIntVar(0, 2, "Num5")
A6 = model.NewIntVar(0, 2, "Num6")
A7 = model.NewIntVar(0, 2, "Num7")
A8 = model.NewIntVar(0, 2, "Num8")
A9 = model.NewIntVar(0, 2, "Num9")

# Antenna 1 connections
model.Add(A1 != A2)
model.Add(A1 != A3)
model.Add(A1 != A4)

# Antenna 2 connections
model.Add(A2 != A1)
model.Add(A2 != A3)
model.Add(A2 != A4)
model.Add(A2 != A5)
model.Add(A2 != A6)

# Antenna 3 connections
model.Add(A3 != A1)
model.Add(A3 != A2)
model.Add(A3 != A6)
model.Add(A3 != A9)

# Antenna 4 connections
model.Add(A4 != A1)
model.Add(A4 != A2)
model.Add(A4 != A5)

# Antenna 5 connections
model.Add(A5 != A2)
model.Add(A5 != A4)

# Antenna 6 connections
model.Add(A6 != A2)
model.Add(A6 != A7)
model.Add(A6 != A8)

# Antenna 7 connections
model.Add(A7 != A6)
model.Add(A7 != A8)

# Antenna 8 connections
model.Add(A8 != A6)
model.Add(A8 != A7)
model.Add(A8 != A9)

# Antenna 9 connections
model.Add(A9 != A3)
model.Add(A9 != A8)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    # print("SF: %s" % colors[solver.Value(SF)])
    # print("Alameda: %s" % colors[solver.Value(Alameda)])
    # print("Marin: %s" % colors[solver.Value(Marin)])
    # print("Contra Costa: %s" % colors[solver.Value(ContraCosta)])
    # print("Solano: %s" % colors[solver.Value(Solano)])
    # print("Sonoma: %s" % colors[solver.Value(Sonoma)])
    # print("Santa Clara: %s" % colors[solver.Value(SantaClara)])
    # print("San Mateo: %s" % colors[solver.Value(SanMateo)])
    # print("Napa: %s" % colors[solver.Value(Napa)])
    
    print("A1: %s" % freqs[solver.Value(A1)])
    print("A2: %s" % freqs[solver.Value(A2)])
    print("A3: %s" % freqs[solver.Value(A3)])
    print("A4: %s" % freqs[solver.Value(A4)])
    print("A5: %s" % freqs[solver.Value(A5)])
    print("A6: %s" % freqs[solver.Value(A6)])
    print("A7: %s" % freqs[solver.Value(A7)])
    print("A8: %s" % freqs[solver.Value(A8)])
    print("A9: %s" % freqs[solver.Value(A9)])

