const fs = require('fs')

let text = fs.readFileSync('scraped.txt').toString()

text = JSON.parse(text)
text = JSON.parse(text)

text = JSON.stringify(text, null, 4)

console.log(text)

