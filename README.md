# attending: the docs in!

A python package which brings better docstrings with an impeccable bedside manner.

The `attending` supervises other docs, and has the last word.

## Improving the quality of resident docs.

It is widely accepted that Python comes with "batteries included", but one could
also argue that "instructions mayb not be included" is a fair asssement.

The CPython community, which develops reference implementation of the
language, prefers the cross-referencing and coherent standalone documentation
provided by [docs.python.org](https://docs.python.org)


The job of the `attending` is to make more documentation available directly in
the REPL.

One of the more ambitious goals of this project is a "No docstring left
as None" policy. A docstring of None is a bug in the standard library.

It's a joy to have usage examples in the docstring of a function. In the
scientific Python community, that is a standard. Guido van Rossum was [asked
this question directly at the first PyData
workshop in 2012](https://youtu.be/QjXJLVINsSA?t=4757), and replied:

    You can't really expect us to write all of the documentation twice. So,
    we've made a very solid commitment to  having external documentaiton. I'm
    not entirely sur ehow to build that interactive system but we can generate
    different formats from the external documentation, its not tied to HTML...

    ...

    I don't think that you can get people to agree that we should abandon the
    practice of writing good external documentation and instead start writing
    good docstrings. It's one or the other, and we have too large an investment
    in tools that do external documentation really well.


## Why's it called `attending`?

<dl>
<dt>attending physician:</dt>
<dd>the physician who is responsible for a particular patient. In a university
hospital setting, an attending physician often also has teaching
responsibilities, holds a faculty appointment, and supervises residents and
medical students. Also called `attending`.</dd>
Mosby's Medical Dictionary
</dl>


