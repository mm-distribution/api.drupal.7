# node_types_rebuild()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 475–477 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L475-L477)
- **Module/theme:** node

## Signature

```php
function node_types_rebuild()
```

## Documentation

```text
Updates the database cache of node types.

All new module-defined node types are saved to the database via a call to
node_type_save(), and obsolete ones are deleted via a call to
node_type_delete(). See _node_types_build() for an explanation of the new
and obsolete types.

@see _node_types_build()
```

## Code

```php
function node_types_rebuild() {
  _node_types_build(TRUE);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
