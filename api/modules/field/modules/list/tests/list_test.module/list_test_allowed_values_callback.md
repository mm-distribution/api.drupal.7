# list_test_allowed_values_callback()

- **Type:** Function
- **File:** [`modules/field/modules/list/tests/list_test.module`](_file.md), lines 11–23 · [local source](../../../../../../../source/modules/field/modules/list/tests/list_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list_test.module#L11-L23)
- **Module/theme:** list_test

## Signature

```php
function list_test_allowed_values_callback($field)
```

## Documentation

```text
Allowed values callback.
```

## Code

```php
function list_test_allowed_values_callback($field) {
  $values = array(
    'Group 1' => array(
      0 => 'Zero',
    ),
    1 => 'One',
    'Group 2' => array(
      2 => 'Some <script>dangerous</script> & unescaped <strong>markup</strong>',
    ),
  );

  return $values;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
