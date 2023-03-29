from typing import Dict, List

def Phi1Phi2_head_print():
    print(f"{'Image name':<11}|{'Phi1':<22}|{'Phi2':<22}")

def Phi1Phi2_info_print(Phi1Phi2: Dict[str, float], standartImageNames: List[str]):

    noDrtift = 1
    print("Standart images:")
    Phi1Phi2_head_print()
    for imageName in Phi1Phi2.keys():
        if (noDrtift and imageName not in standartImageNames):
            noDrtift = 0
            print("\nImages to classify:")
            Phi1Phi2_head_print()
        print(f"{imageName:<11}|{Phi1Phi2[imageName]['Phi1']:<22}|{Phi1Phi2[imageName]['Phi2']:<22}")
    
    print()

def distances_to_standart_Phi1Phi2_head_print(distance_to: str, standartImageNames: List[str]):
    print(f'Distances to {distance_to}:')
    standartImageNamesString = ''.join(f"{standartImageName:<23}{(standartImageNames[-1] != standartImageName) * '|'}" for standartImageName in standartImageNames)
    print(f"{'Image name':<11}|{standartImageNamesString}|{'Class':<6}")

def distances_to_standart_Phi1Phi2_info_print(distances_to_standart_Phi1Phi2: Dict[str, Dict[str, Dict[str, float]]], standartImageNames: List[str], classification: Dict[str, Dict[str, str]]):
    for distance_to in distances_to_standart_Phi1Phi2[list(distances_to_standart_Phi1Phi2.keys())[0]].keys():
        distances_to_standart_Phi1Phi2_head_print(distance_to, standartImageNames)
        for imageName in distances_to_standart_Phi1Phi2.keys():
            distances_to_standart_string = ''.join(f"{str(distances_to_standart_Phi1Phi2[imageName][distance_to][standartImageName]):<23}{(standartImageNames[-1] != standartImageName) * '|'}" for standartImageName in standartImageNames)
            print(f"{imageName:<11}|{distances_to_standart_string}|{classification[imageName][distance_to]}")
        print()