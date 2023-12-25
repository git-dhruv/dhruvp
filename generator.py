"""
Project layout generator 
Its a simple script that gets shit done faster 
"""

import argparse


def main(name):
    text = rf'''
<!-- {name} -->
<tr onmouseout="{name}_stop()" onmouseover="{name}_start()" class="part">
    <td style="padding:1px;width:25%;vertical-align:middle">
    <div class="one">
        <div class="two" id='{name}_image'>
        <img src='images/{name}.gif' width="160">

        </div>
        <img src='images/{name}.gif' width="160">
    </div>
    <script type="text/javascript">
        function {name}_start() {{
        document.getElementById('{name}_image').style.opacity = "1";
        }}

        function {name}_stop() {{
        document.getElementById('{name}_image').style.opacity = "0";
        }}
        {name}_stop()
    </script>
    </td>
    <td style="padding:20px;width:75%;vertical-align:middle">

    <papertitle>Pose Graph Optimization</papertitle>

    <br />

    <a href="https://github.com/git-dhruv/Bayesian-informed-6D-Pose-estimation">Code</a>

    <p></p>
    <p>
        Stuff 
    </p>
    </td>
</tr>'''
    with open('out.txt', "w+") as f:
        f.write(text)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='Name of the Project')

    projectName = f"{parser.parse_args().name}"
    main(projectName)