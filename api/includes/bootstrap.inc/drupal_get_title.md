# drupal_get_title()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2193–2202 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2193-L2202)

## Signature

```php
function drupal_get_title()
```

## Documentation

```text
Gets the title of the current page.

The title is displayed on the page and in the title bar.

@return
  The current page's title.
```

## Code

```php
function drupal_get_title() {
  $title = drupal_set_title();

  // During a bootstrap, menu.inc is not included and thus we cannot provide a title.
  if (!isset($title) && function_exists('menu_get_active_title')) {
    $title = check_plain(menu_get_active_title());
  }

  return $title;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
