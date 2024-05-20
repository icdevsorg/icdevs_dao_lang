# Exit script on error
set -e

# Execute Python script
python3 ./scripts/main.py ./patterns.dot ./content/patterns/output

# Check and log result
if [ $? -ne 0 ]; then
    echo "Python script failed"
    exit 1
fi

# Execute another Python script
python3 inject_front_matter.py

# Build Jekyll site
bundle exec jekyll build