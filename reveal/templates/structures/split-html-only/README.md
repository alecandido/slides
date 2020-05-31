# Split html layout

Each slide or vertical group of slides is in its own file, than can also contain
yaml frontmatter for additional settings to be used in the slide html tag.

## Expected project structure
In the root of your reveal presentation folder is expected the following
files structure:

```
|- src
  |- slides
    |- 1.html
    |- 2.html
    |- ...
```

## Usage
Run `build_templat.py` to build the `index.html` out of your input.
