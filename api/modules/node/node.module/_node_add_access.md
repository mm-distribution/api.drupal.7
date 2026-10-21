# _node_add_access()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1957–1971 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1957-L1971)
- **Module/theme:** node

## Signature

```php
function _node_add_access()
```

## Documentation

```text
Access callback: Checks whether the user has permission to add a node.

@return
  TRUE if the user has add permission, otherwise FALSE.

@see node_menu()
```

## Code

```php
function _node_add_access() {
  $types = node_type_get_types();
  foreach ($types as $type) {
    if (node_hook($type->type, 'form') && node_access('create', $type->type)) {
      return TRUE;
    }
  }
  if (user_access('administer content types')) {
    // There are no content types defined that the user has permission to create,
    // but the user does have the permission to administer the content types, so
    // grant them access to the page anyway.
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
