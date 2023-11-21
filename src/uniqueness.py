from src.puf_data_processor import PUFDataProcessor


class PUFUniquenessCalculator(PUFDataProcessor):
    def __init__(self):
        super().__init__()
        self.val_name = "Uniqueness"

    def process_file(self, file_path):
        """Process a single file."""
        responses = self.load_data(file_path)
        return self.calculate_uniqueness(responses)

    def calculate_uniqueness(self, responses):
        """Compute the Uniqueness for a list of PUF responses."""
        k = len(responses)  # Number of chips
        n = len(
            responses[0]
        )  # Length of each response, assuming all are of equal length
        total_hd = 0  # Total Hamming Distance

        # Compute the total Hamming Distance between all pairs of responses
        for i in range(k - 1):
            for j in range(i + 1, k):
                total_hd += self.hamming_distance(responses[i], responses[j])

        # Calculate the average HD and convert it to percentage
        avg_hd = (2 * total_hd) / (k * (k - 1))
        uniqueness_percentage = (avg_hd / n) * 100

        return uniqueness_percentage
