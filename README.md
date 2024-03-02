# Qrename

Qrename is a powerful tool designed to streamline the process of renaming multiple image files. Whether you're managing a vast local library archive or organizing personal collections, Qrename simplifies the renaming process with efficiency and ease.

## Features

- **Bulk Renaming**: Queue up multiple image files and rename them sequentially with customized names.
- **Image Preview**: Preview each image before renaming, ensuring accuracy in the renaming process.
- **Flexible File Selection**: Select multiple image files at once using a file dialog.
- **Supported Formats**: Qrename supports common image formats such as PNG, JPG, BMP, and JPEG.

## Getting Started

1. **Clone the Repository**: Begin by cloning the Qrename repository to your local machine.

   ```bash
   git clone https://github.com/your-username/qrename.git
   ```

2. **Install Dependencies**: Qrename utilizes PyQt5 for the graphical interface. Ensure you have PyQt5 installed. You can install it via pip:

   ```bash
   pip install pyqt5
   ```

3. **Run Qrename**: Execute the Qrename tool by running the following command:

   ```bash
   python qrename.py
   ```

## Usage

1. **Load Files**: Click on the "Load Files" button to select the images you want to rename. Use the file dialog to navigate to the folder containing your images.

2. **Preview Images**: The selected images will be displayed one by one. Ensure correctness by reviewing each image before renaming.

3. **Rename Images**: Enter the desired name for the image in the text field provided. Press Enter or click the "Rename" button to apply the new name to the image.

4. **Sequential Renaming**: Qrename renames images sequentially based on the order in which they were loaded. After renaming an image, the next image in the queue is automatically displayed.

5. **Track Progress**: Monitor the number of remaining images to be renamed through the "Remaining in Queue" indicator.

6. **Complete**: Once all images have been renamed, Qrename returns to the initial state, ready for the next batch of files.

## Contribution

Contributions to Qrename are welcome! Whether it's bug fixes, feature enhancements, or localization efforts, feel free to contribute by forking the repository and submitting a pull request.

## Releases

You can find pre-packaged releases for Windows and macOS on the [Releases](https://github.com/your-username/qrename/releases) page. Currently, there are no installers available, but packaged versions are provided for convenience. 

## License

Qrename is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

---

Happy Renaming with Qrename! If you encounter any issues or have suggestions for improvement, don't hesitate to reach out. Your feedback is highly appreciated.
