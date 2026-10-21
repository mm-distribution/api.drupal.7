# hook_field_purge_instance()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2677–2681 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2677-L2681)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_purge_instance($instance)
```

## Documentation

```text
Acts when a field instance is being purged.

In field_purge_instance(), after the field instance has been
removed from the database, the field storage module has had a chance to
run its hook_field_storage_purge_instance(), and the field info cache
has been cleared, this hook is invoked on all modules to allow them to
respond to the field instance being purged.

@param $instance
  The instance being purged.
```

## Code

```php
function hook_field_purge_instance($instance) {
  db_delete('my_module_field_instance_info')
    ->condition('id', $instance['id'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_purge_instance()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
