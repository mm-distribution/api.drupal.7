# drupal_set_breadcrumb()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 243–250 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L243-L250)

## Signature

```php
function drupal_set_breadcrumb($breadcrumb = NULL)
```

## Documentation

```text
Sets the breadcrumb trail for the current page.

@param $breadcrumb
  Array of links, starting with "home" and proceeding up to but not including
  the current page.
```

## Code

```php
function drupal_set_breadcrumb($breadcrumb = NULL) {
  $stored_breadcrumb = &drupal_static(__FUNCTION__);

  if (isset($breadcrumb)) {
    $stored_breadcrumb = $breadcrumb;
  }
  return $stored_breadcrumb;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
