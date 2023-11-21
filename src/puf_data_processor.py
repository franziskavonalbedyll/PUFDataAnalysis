import pandas as pd

class PUFDataProcessor:
    @staticmethod
    def hamming_distance(str1, str2):
        """Compute the Hamming distance between two strings."""
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))

    def load_data(self, file_path):
        """Load PUF data from a fixed-width formatted file."""
        df = pd.read_fwf(file_path, header=None)
        return df[0].tolist()

    def process_multiple_files(self, identifiers):
        """Process multiple files / rows."""
        print(f"----------------------------- {self.val_name.upper()} -----------------------------")

        results = {}
        for identifier in identifiers:
            print(f"Computing the {self.val_name} value of {identifier} ...")
            result = self.process_file(identifier)
            results[identifier] = result

        print("\n")
        print(f"Overall average: {sum(results.values()) / len(results.items())}")
        print("\n")
        print("Detailed Results: ")
        self.print_pretty(results)
        return results

    def print_pretty(self, values_dictionary):
        if self.val_name == "Reliability":
            left_column_name = "Chip/Row Number"
            longest_column_length = len(left_column_name)
        else:
            left_column_name = "Filename"
            longest_column_length = max(len(column) for column in values_dictionary.keys())

        # Create the header with proper spacing
        header_spacing = longest_column_length + 10  # Add some extra space for padding
        print(f"{left_column_name:<{header_spacing}}{self.val_name}-Value:")

        for fname, val in values_dictionary.items():
            print(f"{fname:<{header_spacing}}{val}")

        print("\n\n\n")