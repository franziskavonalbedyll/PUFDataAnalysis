from collections import defaultdict

import pandas as pd

from src.puf_data_processor import PUFDataProcessor


class PUFReliabilityCalculator(PUFDataProcessor):
    def __init__(self):
        super().__init__()
        self.val_name = "Reliability"

    @staticmethod
    def get_data_for_chips(file_paths):
        chip_rows = defaultdict(list)
        for row_index in range(256):
            for fpath in file_paths:
                row = pd.read_csv(
                    fpath, header=None, skiprows=row_index, nrows=1
                )
                chip_rows[row_index].append(row.values[0][0])

        return chip_rows

    def compute_reliability(self, responses):
        """Compute the Reliability for a list of PUF responses of the same chip."""
        m = len(responses)  # Number of samples
        n = len(
            responses[0]
        )  # Length of each response, assuming all are of equal length
        total_hd = 0  # Total Hamming Distance

        # Compute the total Hamming Distance for intra-chip (between samples of the same chip)
        for i in range(1, m):
            total_hd += self.hamming_distance(responses[0], responses[i])

        # Calculate the average HD and convert it to percentage
        hd_intra = (total_hd / m) / n * 100

        # Reliability is defined as 100% minus the average intra-chip HD
        reliability_percentage = 100 - hd_intra

        return reliability_percentage

    def compute_reliabilties(self, file_paths):
        reliabilties = {}
        data_by_chip = self.get_data_for_chips(file_paths)

        print(
            f"----------------------------- {self.val_name.upper()} -----------------------------"
        )

        for chip_idx, chip_data in data_by_chip.items():
            reliability = self.compute_reliability(chip_data)
            reliabilties[chip_idx] = reliability

        print("\n")
        print(
            f"Overall average: {sum(reliabilties.values()) / len(reliabilties.items())}"
        )
        print("\n")
        print("Detailed Results: ")
        self.print_pretty(reliabilties)

        return reliabilties
