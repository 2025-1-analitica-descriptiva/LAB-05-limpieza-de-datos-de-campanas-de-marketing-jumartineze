import os


def save_output(data, output_directory, filename):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_path = os.path.join(output_directory, filename)
    data.to_csv(output_path, index=False, encoding="utf-8")