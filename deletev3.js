const fs = require('fs');
const path = require('path');

const targetDirectory = './'; // Replace with your target directory

function deleteTargetFiles(dir) {
    fs.readdir(dir, (err, files) => {
        if (err) {
            console.error(`Error reading directory: ${dir}`, err);
            return;
        }

        files.forEach((file) => {
            const filePath = path.join(dir, file);

            fs.stat(filePath, (err, stat) => {
                if (err) {
                    console.error(`Error stating file: ${filePath}`, err);
                    return;
                }

                if (stat.isDirectory()) {
                    deleteTargetFiles(filePath); // Recursively search the directory
                } else if (stat.isFile()) {
                    if (file.endsWith('_v3.png') || file.endsWith('_v3.dot')) {
                        fs.unlink(filePath, (err) => {
                            if (err) {
                                console.error(`Error deleting file: ${filePath}`, err);
                            } else {
                                console.log(`Deleted file: ${filePath}`);
                            }
                        });
                    }
                }
            });
        });
    });
}

deleteTargetFiles(targetDirectory);
