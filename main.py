from src.uniqueness import PUFUniquenessCalculator
from src.uniformity import PUFUniformityCalculator
from src.reliability import PUFReliabilityCalculator
from src.bit_aliasing import PUFBitAliasingCalculator
from src.file_handler import PUFFileHandler
from src.helpers import load_filepaths_from_directory

# Directories in which the data is stored in
DATA_DIRECTORY = "data"
BIN_DATA_DIRECTORY = "bin_data"

# For each file in DATA_DIRECTORY, convert its data to binary and save it (if it doesn't exist yet)
puf_file_handler = PUFFileHandler(DATA_DIRECTORY, BIN_DATA_DIRECTORY)
puf_file_handler.check_and_convert_files()

# get paths to all converted data files
txt_files = load_filepaths_from_directory(BIN_DATA_DIRECTORY)

# Compute bit-aliasing values
calculator = PUFBitAliasingCalculator()
bitaliasing_values = calculator.process_multiple_files(txt_files)

# Compute reliability values
calculator = PUFReliabilityCalculator()
reliability_values = calculator.compute_reliabilties(txt_files)

# Compute uniqueness values
calculator = PUFUniquenessCalculator()
uniqueness_values = calculator.process_multiple_files(txt_files)

# Compute uniformity values
calculator = PUFUniformityCalculator()
uniformity_values = calculator.process_multiple_files(txt_files)

