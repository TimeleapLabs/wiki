from docutils import nodes
from docutils.parsers.rst import Directive
import random


def chart(src):
    id = '%030x' % random.randrange(16**30)
    return f'''
        <div class="chart" id="chart_{id}"></div>
        <script>
            (() => {{
                const render = () => {{
                    if (window.ApexCharts)
                        fetch("{src}")
                        .then(resp => resp.json())
                        .then(options => new ApexCharts(document.querySelector("#chart_{id}"), options))
                        .then(chart => chart.render());
                    else setTimeout(render, 250);
                }};
                render();
            }})();
        </script>
    '''


class Chart(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        src = self.arguments[0]
        raw = chart(src)
        node = nodes.raw("", raw, format='html')
        return [node]


def setup(app):
    app.add_directive("chart", Chart)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
