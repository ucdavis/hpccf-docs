---
title: Documentation Style Guide
---

## Spelling and Validation

Our build pipeline is set to require strict validation, which means it will fail on certain warnings, such as broken links, absolute links, nonexistent anchors,
and spelling errors. You can disable strict mode locally by running with `mkdocs serve --no-strict`.

The build script will display misspelled words with their line numbers and context.
Inline and code blocks are ignored, as well as URLs.

Extra words can be added to `docs/extra-dictionary.txt`.

!!! note

    Due to limitations of the spellchecker, when a misspelled word _outside_ a
    code block is discovered, _all_ instances of the word will be highlighted in the output.
    For example, if you fail to backtick `sbatch` in your text, any `#SBATCH` lines in
    example code within the same file will also be highlighted. The code-block instances
    do not need to be corrected.

## Links, URLs, and Emails

All links and URLs should be wrapped in link syntax, that is, `[display text](URL or link)`.
Emails should be given `mailto:` links, like `[person@example.com](mailto:person@example.com)`.

For example, consider the following directory layout:

```
docs
├── a
│   └── foo.md
└── b
    └── bar.md
```

A link within `foo.md` pointing to `bar.md` should be formatted:

```
Check out our information concerning [bars](../b/bar.md)!
```

Let's say `bar.md` has sections:

```
## Blorp

Some blorps blap.

## Bloop

Bloops _never_ blap.
```

A link directly to one of the sections can be created with an anchor:

```
For more details, please see the section on [bloops](../b/bar.md#bloop).
```

More information can be found in the [MkDocs documentation](https://www.mkdocs.org/user-guide/writing-your-docs/#linking-to-pages).

!!! note

    The spellchecker will often discover bare URLs for you on accident. If you properly wrap
    your URLs in link syntax, the spellchecker will ignore them. Do _not_ just add the URL
    components to the dictionary.

## Executables

Executable names should be formatted with inline code ticks. Many executable names will be
hit by the spellchecker; do not just add the executable name to the dictionary. For example, this is wrong, and will emit a spelling failure:

```
When using sbatch, be sure to...
```

But this will not:

```
When using `sbatch`, be sure to...
```

## Formatting

### Markdown

Section headings should start at the second level: `##`, not `#`. The single hash is reserved for
page titles.

Make sure that your headings have a space after the hashes: `## Section`, not `##Section`.

### `mkdocs.yaml`

Please use two spaces per tab in the configuration file.
