# menu_tab_root_path()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2277–2280 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2277-L2280)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tab_root_path()
```

## Documentation

```text
Returns the router path, or the path for a default local task's parent.
```

## Code

```php
function menu_tab_root_path() {
  $links = menu_local_tasks();
  return $links['root_path'];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
