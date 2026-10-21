# hook_field_purge_field()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2659–2663 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2659-L2663)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_crud](../../../topics/field_crud.md)

## Signature

```php
function hook_field_purge_field($field)
```

## Documentation

```text
Acts when a field record is being purged.

In field_purge_field(), after the field configuration has been
removed from the database, the field storage module has had a chance to
run its hook_field_storage_purge_field(), and the field info cache
has been cleared, this hook is invoked on all modules to allow them to
respond to the field being purged.

@param $field
  The field being purged.
```

## Code

```php
function hook_field_purge_field($field) {
  db_delete('my_module_field_info')
    ->condition('id', $field['id'])
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_purge_field()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
