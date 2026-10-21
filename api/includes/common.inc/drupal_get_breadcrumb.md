# drupal_get_breadcrumb()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 255–263 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L255-L263)

## Signature

```php
function drupal_get_breadcrumb()
```

## Documentation

```text
Gets the breadcrumb trail for the current page.
```

## Code

```php
function drupal_get_breadcrumb() {
  $breadcrumb = drupal_set_breadcrumb();

  if (!isset($breadcrumb)) {
    $breadcrumb = menu_get_active_breadcrumb();
  }

  return $breadcrumb;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
