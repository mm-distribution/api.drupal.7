# _statistics_link()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 401–405 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L401-L405)
- **Module/theme:** statistics

## Signature

```php
function _statistics_link($path, $width = 35)
```

## Documentation

```text
Generates a link to a path, truncating the displayed text to a given width.

@param $path
  The path to generate the link for.
@param $width
  The width to set the displayed text of the path.

@return
  A string as a link, truncated to the width, linked to the given $path.
```

## Code

```php
function _statistics_link($path, $width = 35) {
  $title = drupal_get_path_alias($path);
  $title = truncate_utf8($title, $width, FALSE, TRUE);
  return l($title, $path);
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
