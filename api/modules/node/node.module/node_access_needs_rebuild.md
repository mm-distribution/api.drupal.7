# node_access_needs_rebuild()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3591–3601 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3591-L3601)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function node_access_needs_rebuild($rebuild = NULL)
```

## Documentation

```text
Flags or unflags the node access grants for rebuilding.

If the argument isn't specified, the current value of the flag is returned.
When the flag is set, a message is displayed to users with 'access
administration pages' permission, pointing to the 'rebuild' confirm form.
This can be used as an alternative to direct node_access_rebuild calls,
allowing administrators to decide when they want to perform the actual
(possibly time consuming) rebuild. When unsure if the current user is an
administrator, node_access_rebuild() should be used instead.

@param $rebuild
  (Optional) The boolean value to be written.

@return
  The current value of the flag if no value was provided for $rebuild.

@see node_access_rebuild()
```

## Code

```php
function node_access_needs_rebuild($rebuild = NULL) {
  if (!isset($rebuild)) {
    return variable_get('node_access_needs_rebuild', FALSE);
  }
  elseif ($rebuild) {
    variable_set('node_access_needs_rebuild', TRUE);
  }
  else {
    variable_del('node_access_needs_rebuild');
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
