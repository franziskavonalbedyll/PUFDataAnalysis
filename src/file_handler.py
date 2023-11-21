import os

import pandas as pd


class PUFFileHandler:
    def __init__(self, data_dir, data_bin_dir):
        self.data_dir = data_dir
        self.data_bin_dir = data_bin_dir

    @staticmethod
    def hex_to_binary(hex_string):
        """Convert a hexadecimal string to a binary string."""
        binary_string = bin(int(hex_string, 16))[
            2:
        ]  # Convert hex to binary and remove the '0b' prefix
        return binary_string.zfill(
            len(hex_string) * 4
        )  # Pad with zeros to maintain the bit length

    def load_data(self, file_path):
        """Load PUF data from a fixed-width formatted file and convert it to binary."""
        df = pd.read_fwf(file_path, header=None)
        return df[0].apply(self.hex_to_binary).tolist()

    def check_and_convert_files(self):
        """Check if each file in data_dir has a corresponding binary file in data_bin_dir."""
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".txt"):
                base_name = os.path.splitext(filename)[0]
                corresponding_bin_file = f"{base_name}_bin.txt"
                corresponding_bin_path = os.path.join(
                    self.data_bin_dir, corresponding_bin_file
                )

                # Check if the binary file does not exist
                if not os.path.exists(corresponding_bin_path):
                    print(
                        f"File {corresponding_bin_file} doesn't exist yet, creating it right now ..."
                    )
                    # Call the function to convert and save the binary file
                    self.convert_and_save_file(
                        os.path.join(self.data_dir, filename),
                        corresponding_bin_path,
                    )

    def convert_and_save_file(self, hex_file_path, bin_file_path):
        """Convert a file with hexadecimal strings to binary and save it to the specified path."""
        binary_data = self.load_data(hex_file_path)
        with open(bin_file_path, "w") as f:
            for binary_string in binary_data:
                f.write(f"{binary_string}\n")
