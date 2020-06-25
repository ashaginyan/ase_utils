import numpy as np


def get_radius_centered(pos):
    return (pos[0]**2 + pos[1]**2 + pos[2]**2)**0.5

def cut_atoms(poss, r):
    poss_cut = []
    for pos in poss:
        if get_radius_centered(pos) < r:
            poss_cut.append(pos)
    poss_cut = np.array(poss_cut)
    return poss_cut

def cut_atoms_inside(poss, r):
    poss_cut = []
    for pos in poss:
        if get_radius_centered(pos) > r:
            poss_cut.append(pos)
    poss_cut = np.array(poss_cut)
    return poss_cut
