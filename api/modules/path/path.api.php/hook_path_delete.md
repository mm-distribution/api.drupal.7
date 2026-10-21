# hook_path_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/path/path.api.php`](_file.md), lines 65–69 · [local source](../../../../source/modules/path/path.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.api.php#L65-L69)
- **Module/theme:** path
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_path_delete($path)
```

## Documentation

```text
Respond to a path being deleted.

@param $path
  An associative array containing the following keys:
  - source: The internal system path.
  - alias: The URL alias.
  - pid: Unique path alias identifier.
  - language: The language of the alias.

@see path_delete()
```

## Code

```php
function hook_path_delete($path) {
  db_delete('mytable')
    ->condition('pid', $path['pid'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_path_delete()".

_None found._

---
_Drupal 7.103 · [modules/path/path.api.php](https://github.com/drupal/drupal/blob/7.103/modules/path/path.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
