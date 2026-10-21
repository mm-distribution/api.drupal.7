# themes/bartik/templates/comment-wrapper.tpl.php

- **Source:** [local](../../../../../source/themes/bartik/templates/comment-wrapper.tpl.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/themes/bartik/templates/comment-wrapper.tpl.php) · 51 lines
- **Module/theme:** bartik

## File documentation

```text
@file
Bartik's theme implementation to provide an HTML container for comments.

Available variables:
- $content: The array of content-related elements for the node. Use
  render($content) to print them all, or
  print a subset such as render($content['comment_form']).
- $classes: String of classes that can be used to style contextually through
  CSS. It can be manipulated through the variable $classes_array from
  preprocess functions. The default value has the following:
  - comment-wrapper: The current template type, i.e., "theming hook".
- $title_prefix (array): An array containing additional output populated by
  modules, intended to be displayed in front of the main title tag that
  appears in the template.
- $title_suffix (array): An array containing additional output populated by
  modules, intended to be displayed after the main title tag that appears in
  the template.

The following variables are provided for contextual information.
- $node: Node object the comments are attached to.
The constants below the variables show the possible values and should be
used for comparison.
- $display_mode
  - COMMENT_MODE_FLAT
  - COMMENT_MODE_THREADED

Other variables:
- $classes_array: Array of html class attribute values. It is flattened
  into a string within the variable $classes.

@see template_preprocess_comment_wrapper()
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
