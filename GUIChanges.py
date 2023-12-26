from IPython.display import Javascript
Javascript("""
    document.querySelector("#jp-NotebookLogo > svg:nth-child(1)").remove()
    let img = document.createElement('img');
    img.src = "https://static.wixstatic.com/media/4db827_66a45f3761ec478fa11c2ee044757ab8%7Emv2.png/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/4db827_66a45f3761ec478fa11c2ee044757ab8%7Emv2.png";
    document.querySelector("#jp-NotebookLogo").append(img)
""")

from IPython.display import HTML
HTML("""
<style>
    div.jp-Cell-inputWrapper:nth-child(3) > div:nth-child(1) > div:nth-child(1) { background-color:grey !important; }
    div.jp-Cell-outputWrapper:nth-child(5) > div:nth-child(1) > div:nth-child(1) { background-color:transparent !important; }
    div.jp-Cell-outputWrapper:nth-child(5) > div:nth-child(1) { background-color:transparent !important; }
    #jp-NotebookLogo > svg:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(2)
</style>
""")
