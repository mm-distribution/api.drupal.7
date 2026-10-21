# menu_set_active_item()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2364–2369 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2364-L2369)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_set_active_item($path)
```

## Documentation

```text
Sets the active path, which determines which page is loaded.

Note that this may not have the desired effect unless invoked very early
in the page load, such as during hook_boot(), or unless you call
menu_execute_active_handler() to generate your page output.

@param $path
  A Drupal path - not a path alias.
```

## Code

```php
function menu_set_active_item($path) {
  $_GET['q'] = $path;
  // Since the active item has changed, the active menu trail may also be out
  // of date.
  drupal_static_reset('menu_set_active_trail');
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
