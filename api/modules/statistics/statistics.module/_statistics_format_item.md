# _statistics_format_item()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 418–423 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L418-L423)
- **Module/theme:** statistics

## Signature

```php
function _statistics_format_item($title, $path)
```

## Documentation

```text
Formats an item for display, including both the item title and the link.

@param $title
  The text to link to a path; will be truncated to a maximum width of 35.
@param $path
  The path to link to; will default to '/'.

@return
  An HTML string with $title linked to the $path.
```

## Code

```php
function _statistics_format_item($title, $path) {
  $path = ($path ? $path : '/');
  $output  = ($title ? "$title<br />" : '');
  $output .= _statistics_link($path);
  return $output;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
