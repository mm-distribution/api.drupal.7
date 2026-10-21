# field_update_7003()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 466–468 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L466-L468)
- **Module/theme:** field
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function field_update_7003()
```

## Documentation

```text
Add the FieldInfo class to the class registry.
```

## Code

```php
function field_update_7003() {
  // Empty update to force a rebuild of the registry.
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
