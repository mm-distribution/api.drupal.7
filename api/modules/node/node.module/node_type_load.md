# node_type_load()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 489–491 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L489-L491)
- **Module/theme:** node

## Signature

```php
function node_type_load($name)
```

## Documentation

```text
Menu argument loader: loads a node type by string.

@param $name
  The machine-readable name of a node type to load, where '_' is replaced
  with '-'.

@return
  A node type object or FALSE if $name does not exist.
```

## Code

```php
function node_type_load($name) {
  return node_type_get_type(strtr($name, array('-' => '_')));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
