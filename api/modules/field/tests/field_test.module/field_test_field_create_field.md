# field_test_field_create_field()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 180–183 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L180-L183)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_field_create_field($field)
```

## Documentation

```text
Memorize calls to hook_field_create_field().
```

## Code

```php
function field_test_field_create_field($field) {
  $args = func_get_args();
  field_test_memorize(__FUNCTION__, $args);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
