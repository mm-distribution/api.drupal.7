# filter_tips_long()

- **Type:** Function
- **File:** [`modules/filter/filter.pages.inc`](_file.md), lines 17–25 · [local source](../../../../source/modules/filter/filter.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.pages.inc#L17-L25)
- **Module/theme:** filter

## Signature

```php
function filter_tips_long($format = NULL)
```

## Documentation

```text
Page callback: Displays a page with long filter tips.

@return string
  An HTML-formatted string.

@see filter_menu()
@see theme_filter_tips()
```

## Code

```php
function filter_tips_long($format = NULL) {
  if (!empty($format)) {
    $output = theme('filter_tips', array('tips' => _filter_tips($format->format, TRUE), 'long' => TRUE));
  }
  else {
    $output = theme('filter_tips', array('tips' => _filter_tips(-1, TRUE), 'long' => TRUE));
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/filter/filter.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
