# menu_secondary_local_tasks()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2260–2264 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2260-L2264)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_secondary_local_tasks()
```

## Documentation

```text
Returns the rendered local tasks at the second level.
```

## Code

```php
function menu_secondary_local_tasks() {
  $links = menu_local_tasks(1);
  // Do not display single tabs.
  return ($links['tabs']['count'] > 1 ? $links['tabs']['output'] : '');
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
