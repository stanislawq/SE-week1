"""
Main module.
"""
from varasto import Varasto

def main():
    """
    Main function.
    """
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Initial: Mehu: {mehua}, Olut: {olutta}")

    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehu after ops: {mehua}")

    print(f"Error test: {Varasto(-100.0)}")

    olutta.lisaa_varastoon(1000.0)
    print(f"Olut after overflow: {olutta}")

if __name__ == "__main__":
    main()
