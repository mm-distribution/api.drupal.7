# _filter_url_escape_comments()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1652–1677 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1652-L1677)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url_escape_comments($match, $escape = NULL)
```

## Documentation

```text
Escapes the contents of HTML comments.

Callback for preg_replace_callback() within _filter_url().

@param $match
  An array containing matches to replace from preg_replace_callback(),
  whereas $match[1] is expected to contain the content to be filtered.
@param $escape
  (optional) A Boolean indicating whether to escape (TRUE) or unescape
  comments (FALSE). Defaults to NULL, indicating neither. If TRUE, statically
  cached $comments are reset.
```

## Code

```php
function _filter_url_escape_comments($match, $escape = NULL) {
  static $mode, $comments = array();

  if (isset($escape)) {
    $mode = $escape;
    if ($escape){
      $comments = array();
    }
    return;
  }

  // Replace all HTML coments with a '<!-- [hash] -->' placeholder.
  if ($mode) {
    $content = $match[1];
    $hash = hash('sha256', $content);
    $comments[$hash] = $content;
    return "<!-- $hash -->";
  }
  // Or replace placeholders with actual comment contents.
  else {
    $hash = $match[1];
    $hash = trim($hash);
    $content = $comments[$hash];
    return "<!--$content-->";
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
