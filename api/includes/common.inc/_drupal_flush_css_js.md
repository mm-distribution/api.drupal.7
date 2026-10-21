# _drupal_flush_css_js()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7891–7894 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7891-L7894)

## Signature

```php
function _drupal_flush_css_js()
```

## Documentation

```text
Changes the dummy query string added to all CSS and JavaScript files.

Changing the dummy query string appended to CSS and JavaScript files forces
all browsers to reload fresh files.
```

## Code

```php
function _drupal_flush_css_js() {
  // The timestamp is converted to base 36 in order to make it more compact.
  variable_set('css_js_query_string', base_convert(REQUEST_TIME, 10, 36));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
