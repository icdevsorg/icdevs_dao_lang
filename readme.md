python3 ./scripts/main.py ./patterns.dot ./content/patterns/output
python3 inject_front_matter.py

https://stackoverflow.com/questions/40266604/pip-install-pygraphviz-fails-failed-building-wheel-for-pygraphviz

python3 -m pip install -U --no-cache-dir  \
            --config-settings="--global-option=build_ext" \
            --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
            --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
            pygraphviz



Here is the hand-drawn sketch in the style of Egon Schiele, depicting a symbolic council or meeting setting to represent transparent governance. The drawing includes expressive, angular lines and dynamic compositions, with elements like open books and visible chains symbolizing blockchain technology. This image captures the ethos of clear and verifiable decision-making processes, with sharp contrasts to highlight transparency and the shadows of doubt.