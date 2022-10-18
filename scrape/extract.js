const load_html = async () => {
    let html_r = await fetch('notion2.html')

    let html = await html_r.text()

    document.querySelector('#host').innerHTML = html
}

const run_extractor = host => {
    let out = {}

    for (let el of host.children) {
        let key = el.children[0].innerText.split('\n')[0]

        console.log('key', key)

        let vals = el.children[1].querySelectorAll('.notranslate')

        let out_v = []
        for (let val of vals) {
            if (val.innerText.length > 0) {
                out_v.push(val.innerText)
            }
        }

        console.log(out_v)

        out[key] = out_v

    }

    return out
}

const load = async () => {
    await load_html()

    const host = document.querySelector('#host')
    let output = run_extractor(host)

    document.querySelector('#output').value = JSON.stringify(output, null, 4)
}

load()

