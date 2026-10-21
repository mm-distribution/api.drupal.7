# field_cache_clear()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 744–747 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L744-L747)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_cache_clear()
```

## Documentation

```text
Clear the field info and field data caches.
```

## Code

```php
function field_cache_clear() {
  cache_clear_all('*', 'cache_field', TRUE);
  field_info_cache_clear();
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
