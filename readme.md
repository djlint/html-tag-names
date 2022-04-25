<h1 align="center">HTML Tag Names</h1>

<h4 align="center">List of known HTML tag names.</h4>

<h5 align="center">Python port of npm package <a href="https://www.npmjs.com/package/html-tag-names" target="_blank">html-tag-names</a>.</h5>

<p align="center">
  <a href="https://pypi.org/project/html-tag-names/">
    <img src="https://badgen.net/pypi/v/html-tag-names" alt="Pypi Version">
  </a>
  <a href="https://pepy.tech/project/html-tag-names">
    <img src="https://static.pepy.tech/badge/html-tag-names" alt="Downloads">
  </a>
</p>


## 🤔 What is this?

This is a list of HTML tag names.
It includes ancient (for example, `nextid` and `basefont`) and modern (for
example, `shadow` and `template`) names from the HTML living standard.
The repo includes scripts to regenerate the data from the specs.

## ⌚ When should I use this?

You can use this package when you need to know what tag names are allowed in
any version of HTML.

## 💾 Install

```sh
pip install html-tag-names

# or

poetry add html-tag-names
```

## ✨ How to Use

```py
from HtmlTagNames import html_tag_names

print(len(html_tag_names)) # => 148

print(html_tag_names[:20])
```

Yields:

```py
[
  'a',
  'abbr',
  'acronym',
  'address',
  'applet',
  'area',
  'article',
  'aside',
  'audio',
  'b',
  'base',
  'basefont',
  'bdi',
  'bdo',
  'bgsound',
  'big',
  'blink',
  'blockquote',
  'body',
  'br'
]
```
## 🪪 License

- [GPL][license] © Riverside Healthcare
- Ported from `html-tag-names` [MIT][LICENSE] © [Titus Wormer](https://github.com/wooorm)

[license]: LICENSE
