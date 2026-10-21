# hook_field_storage_purge_field_instance()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2713–2717 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2713-L2717)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_purge_field_instance($instance)
```

## Documentation

```text
Remove field storage information when a field instance is purged.

Called from field_purge_instance() to allow the field storage module
to remove field instance information when a field instance is being
purged.

@param $instance
  The instance being purged.

@ingroup field_storage
```

## Code

```php
function hook_field_storage_purge_field_instance($instance) {
  db_delete('my_module_field_instance_info')
    ->condition('id', $instance['id'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_purge_field_instance()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
