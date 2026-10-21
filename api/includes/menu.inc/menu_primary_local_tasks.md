# menu_primary_local_tasks()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2251–2255 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2251-L2255)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_primary_local_tasks()
```

## Documentation

```text
Returns the rendered local tasks at the top level.
```

## Code

```php
function menu_primary_local_tasks() {
  $links = menu_local_tasks(0);
  // Do not display single tabs.
  return ($links['tabs']['count'] > 1 ? $links['tabs']['output'] : '');
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
