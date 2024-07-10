
This is s living document! Please contribute and send pull requests.

Thank you to https://github.com/dfinity for the grant that funded much of this work.


Some important commands:


python3 ./scripts/main.py ./patterns.dot ./content/patterns/output
python3 inject_front_matter.py

https://stackoverflow.com/questions/40266604/pip-install-pygraphviz-fails-failed-building-wheel-for-pygraphviz

python3 -m pip install -U --no-cache-dir  \
            --config-settings="--global-option=build_ext" \
            --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
            --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
            pygraphviz
