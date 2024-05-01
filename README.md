# Qrename

Qrename is a powerful tool designed to streamline the process of renaming multiple image files. Whether you're managing a vast local library archive or organizing personal collections, Qrename simplifies the renaming process with efficiency and ease.

![Qrename Logo](Qrename_Logo.jpeg)

## Features

- **Bulk Renaming**: Queue up multiple image files and rename them individually with individualized names.
- **Image Preview**: Preview each image before renaming, ensuring accuracy in the renaming process.
- **Flexible File Selection**: Select multiple image files at once using a file dialog.
- **Supported Formats**: Qrename supports common image formats such as PNG, JPG, BMP, and JPEG.

## Getting Started

Qrename is a fully portable tool, requiring no installation or setup. It provides builds for Windows, Linux, and macOS platforms, ensuring compatibility across different operating systems.

### Using Pre-built Binaries

To get started quickly, download the appropriate binary for your operating system from the [Releases](https://github.com/asorge29/Qrename/releases) page on GitHub. Once downloaded, simply unzip the file and run Qrename directly without any installation process.

### Building from Source

For advanced users or those who prefer to build from source, Qrename's codebase is available on GitHub. Follow these steps to build Qrename locally:

1. **Clone the Repository**: Clone the Qrename repository to your local machine using Git.

```bash
git clone https://github.com/asorge29/Qrename.git
```

2. **Install Dependencies**: Ensure you have Python installed on your system. Navigate to the cloned repository directory and install the required dependencies using pip.

```bash
pip install -r requirements.txt
```


3. **Build with PyInstaller**: Use PyInstaller to create a standalone executable for your platform. Run the following command:

```bash
pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/path/to/cloned/repo/Qrename/qrename_logo_icon.ico" --splash "C:/Users/path/to/cloned/repo/Qrename/Qrename_Logo.jpeg" --add-data "C:/Users/path/to/cloned/repo/Qrename/Qrename_Logo.jpeg;."  "C:/Users/path/to/cloned/repo/Qrename/Qrename.py"
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This command will generate the executable file in the `dist` directory.

4. **Alternative: Auto Py to Exe**: Alternatively, if you prefer using Auto Py to Exe, you can utilize the provided configuration file (`auto-py-to-exe qrename onefile.json`) to build Qrename. Simply open Auto Py to Exe, load the configuration file, and generate the executable.

Ensure to replace `"path/to/cloned/repo"` with the actual path to your cloned repository in the JSON configuration file or in the command above.

Note: When building locally on MacOS, it is necessary to omit the splash screen and use the icon file ending in `.icns` rather than `.ico`

By following these steps, you can build Qrename locally and customize it according to your preferences.

## Usage

1. **Load Files**: Click on the "Load Files" button to select the images you want to rename. Use the file dialog to navigate to the folder containing your images.

2. **Preview Images**: The selected images will be displayed one by one. Ensure correctness by reviewing each image before renaming.

3. **Rename or Delete Images**: Enter the desired name for the image in the text field provided. Press Enter or click the "Rename" button to apply the new name to the image. If you decide you would nto like to keep the image, press the delete button to permanately delete it.

4. **Sequential Renaming**: Qrename renames images sequentially based on the order in which they were loaded. After renaming an image, the next image in the queue is automatically displayed.

5. **Track Progress**: Monitor the number of remaining images to be renamed through the "Remaining in Queue" indicator.

6. **Complete**: Once all images have been renamed, Qrename returns to the initial state, ready for the next batch of files.

## Contribution

Contributions to Qrename are welcome! Whether it's bug fixes, feature enhancements, or localization efforts, feel free to contribute by forking the repository and submitting a pull request.

## License

Qrename is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.