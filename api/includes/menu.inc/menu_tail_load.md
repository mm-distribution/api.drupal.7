# menu_tail_load()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 853–857 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L853-L857)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tail_load($arg, &$map, $index)
```

## Documentation

```text
Loads the path as one string relative to the current index.

To use this load function, you must specify the load arguments
in the router item as:
@code
$item['load arguments'] = array('%map', '%index');
@endcode

@see search_menu().
```

## Code

```php
function menu_tail_load($arg, &$map, $index) {
  $arg = implode('/', array_slice($map, $index));
  $map = array_slice($map, 0, $index);
  return $arg;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
