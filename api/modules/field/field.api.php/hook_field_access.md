# hook_field_access()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2777–2782 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2777-L2782)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_access($op, $field, $entity_type, $entity, $account)
```

## Documentation

```text
Determine whether the user has access to a given field.

This hook is invoked from field_access() to let modules block access to
operations on fields. If no module returns FALSE, the operation is allowed.

@param $op
  The operation to be performed. Possible values: 'edit', 'view'.
@param $field
  The field on which the operation is to be performed.
@param $entity_type
  The type of $entity; for example, 'node' or 'user'.
@param $entity
  (optional) The entity for the operation.
@param $account
  (optional) The account to check; if not given use currently logged in user.

@return
  TRUE if the operation is allowed, and FALSE if the operation is denied.

@ingroup field_types
```

## Code

```php
function hook_field_access($op, $field, $entity_type, $entity, $account) {
  if ($field['field_name'] == 'field_of_interest' && $op == 'edit') {
    return user_access('edit field of interest', $account);
  }
  return TRUE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_access()".

- [field_test_field_access()](../tests/field_test.field.inc/field_test_field_access.md) — `modules/field/tests/field_test.field.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
