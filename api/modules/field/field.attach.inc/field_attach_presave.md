# field_attach_presave()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 913–918 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L913-L918)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_presave($entity_type, $entity)
```

## Documentation

```text
Perform necessary operations just before fields data get saved.

We take no specific action here, we just give other
modules the opportunity to act.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to process.
```

## Code

```php
function field_attach_presave($entity_type, $entity) {
  _field_invoke('presave', $entity_type, $entity);

  // Let other modules act on presaving the entity.
  module_invoke_all('field_attach_presave', $entity_type, $entity);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
