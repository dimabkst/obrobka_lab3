from typing import Dict, List

def Phi1Phi2_head_print():
    print(f"{'Image name':<11}|{'Phi1':<22}|{'Phi2':<22}")

def Phi1Phi2_info_print(Phi1Phi2: Dict[str, float], imageNames: List[str], standartImageNames: List[str]):

    noDrtift = 1
    print("Standart images:")
    Phi1Phi2_head_print()
    for imageName in imageNames:
        if (noDrtift and imageName not in standartImageNames):
            noDrtift = 0
            print("\nImages to classify:")
            Phi1Phi2_head_print()
        print(f"{imageName:<11}|{Phi1Phi2[imageName]['Phi1']:<22}|{Phi1Phi2[imageName]['Phi2']:<22}")
    
    print()