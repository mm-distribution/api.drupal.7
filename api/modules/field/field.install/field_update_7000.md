# field_update_7000()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 399–406 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L399-L406)
- **Module/theme:** field
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function field_update_7000()
```

## Documentation

```text
Field update version placeholder.
```

## Code

```php
function field_update_7000() {
  // Some update helper functions (such as _update_7000_field_create_field())
  // modify the database directly. They can be used safely only if the database
  // schema matches the field module schema established for Drupal 7.0 (i.e.
  // version 7000). This function exists solely to set the schema version to
  // 7000, so that update functions calling those helpers can do so safely
  // by declaring a dependency on field_update_7000().
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
