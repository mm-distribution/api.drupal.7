# field_access()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 997–1012 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L997-L1012)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_access($op, $field, $entity_type, $entity = NULL, $account = NULL)
```

## Documentation

```text
Determine whether the user has access to a given field.

This function does not determine whether access is granted to the entity
itself, only the specific field. Callers are responsible for ensuring that
entity access is also respected. For example, when checking field access for
nodes, check node_access() before checking field_access(), and when checking
field access for entities using the Entity API contributed module,
check entity_access() before checking field_access().

@param $op
  The operation to be performed. Possible values:
  - 'edit'
  - 'view'
@param $field
  The full field structure array for the field on which the operation is to
  be performed. See field_info_field().
@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  (optional) The entity for the operation.
@param $account
  (optional) The account to check, if not given use currently logged in user.

@return
  TRUE if the operation is allowed;
  FALSE if the operation is denied.
```

## Code

```php
function field_access($op, $field, $entity_type, $entity = NULL, $account = NULL) {
  global $user;

  if (!isset($account)) {
    $account = $user;
  }

  foreach (module_implements('field_access') as $module) {
    $function = $module . '_field_access';
    $access = $function($op, $field, $entity_type, $entity, $account);
    if ($access === FALSE) {
      return FALSE;
    }
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
