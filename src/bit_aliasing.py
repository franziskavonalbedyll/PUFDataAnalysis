from src.puf_data_processor import PUFDataProcessor


class PUFBitAliasingCalculator(PUFDataProcessor):
    def __init__(self):
        super().__init__()
        self.val_name = "Bit-Aliasing"

    def process_file(self, file_path):
        """Process a single file."""
        responses = self.load_data(file_path)
        return self.calculate_bitaliasing(responses)

    def calculate_bitaliasing(self, responses):
        """
        Calculate the bit-aliasing for each bit position in the PUF responses.

        :param responses: A list of binary strings representing the PUF responses
        :return: A list of bit-aliasing percentages for each bit position
        """
        k = len(responses)  # Number of PUF responses
        n = len(responses[0])  # Number of bits in each response
        bit_aliasing_percentages = []

        # Iterate over each bit position
        for i in range(n):
            # Count the number of '1's at the current bit position across all responses
            count_ones = sum(response[i] == "1" for response in responses)

            # Calculate the bit-aliasing percentage for this bit position
            bit_aliasing_percentage = (count_ones / k) * 100
            bit_aliasing_percentages.append(bit_aliasing_percentage)

        return sum(bit_aliasing_percentages) / n
