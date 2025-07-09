from analysis.metrics import MoleculeProperties
from analysis.docking import calculate_gnina


def gnina(mol, **kwargs):
    return -calculate_gnina(mol, rec_file=kwargs['pdbfile'])


def sa(mol, **kwargs):
    return MoleculeProperties().calculate_sa(mol)


def qed(mol, **kwargs):
    return MoleculeProperties().calculate_qed(mol)


function = {'gnina': gnina,
            'sa': sa,
            'qed': qed}
