from rdkit import Chem
from rdkit.Chem import Descriptors
def calculate_lipinski(smiles: str) -> dict:
    """
    Calcule les 4 descripteurs de la règle de Lipinski pour une molécule SMILES.
    
    Returns:
        dict: Dictionnaire contenant les descripteurs et le statut du filtre.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)

    # Règle de Lipinski (Rule of 5)
    passes = (mw <= 500) and (logp <= 5) and (hbd <= 5) and (hba <= 10)

    return {
        "MW": round(mw, 2),
        "LogP": round(logp, 2),
        "HBD": hbd,
        "HBA": hba,
        "Passes_Lipinski": passes
    }

if __name__ == "__main__":
    # Molécule de test : Aspirine
    test_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    result = calculate_lipinski(test_smiles)
    print(f"Résultat pour l'Aspirine : {result}")