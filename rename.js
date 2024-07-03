const fs = require('fs');
const path = require('path');

// Function to find and rename files recursively
const findAndRenameFiles = (directory) => {
    fs.readdir(directory, { withFileTypes: true }, (err, files) => {
        if (err) {
            console.error(`Error reading directory ${directory}:`, err);
            return;
        }

        files.forEach((file) => {
            const fullPath = path.join(directory, file.name);

            if (file.isDirectory()) {
                // Recurse into subdirectory
                findAndRenameFiles(fullPath);
            } else if (file.isFile() && file.name.endsWith('_v3.png')) {
                // Compute the new file name
                const newFileName = file.name.replace('_v3.png', '.png');
                const newFullPath = path.join(directory, newFileName);

                // Rename the file
                fs.rename(fullPath, newFullPath, (err) => {
                    if (err) {
                        console.error(`Error renaming file ${fullPath} to ${newFullPath}:`, err);
                    } else {
                        console.log(`Renamed ${fullPath} to ${newFullPath}`);
                    }
                });
            }
        });
    });
};

// Directory to search
const directoryToSearch = './';

// Start the search and rename process
findAndRenameFiles(directoryToSearch);
