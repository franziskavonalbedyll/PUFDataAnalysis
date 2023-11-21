from src.puf_data_processor import PUFDataProcessor

class PUFUniformityCalculator(PUFDataProcessor):
    def __init__(self):
        super().__init__()
        self.val_name = "Uniformity"

    def process_file(self, file_path):
        """Process a single file."""
        responses = self.load_data(file_path)
        return self.get_uniformity_average_over_file(responses)

    def get_uniformity_average_over_file(self, responses):
        uniformity = 0
        for response in responses:
            uniformity += self.calculate_uniformity(response)

        return uniformity / len(responses)


    def calculate_uniformity(self, puf_response):
        """
        Calculate the uniformity of a PUF response.
        :param puf_response: A string representing the binary PUF response
        :return: The uniformity percentage of the PUF response
        """

        # Hamming Weight is simply the number of '1's in the binary string
        hamming_weight = puf_response.count('1')
        n = len(puf_response)  # Total number of bits

        # Calculate the uniformity as defined
        uniformity_percentage = (hamming_weight / n) * 100

        return uniformity_percentage

