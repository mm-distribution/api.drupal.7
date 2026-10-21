# drupal_get_html_head()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 352–356 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L352-L356)

## Signature

```php
function drupal_get_html_head()
```

## Documentation

```text
Retrieves output to be displayed in the HEAD tag of the HTML page.
```

## Code

```php
function drupal_get_html_head() {
  $elements = drupal_add_html_head();
  drupal_alter('html_head', $elements);
  return drupal_render($elements);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
