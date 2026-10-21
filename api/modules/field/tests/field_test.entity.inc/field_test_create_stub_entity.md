# field_test_create_stub_entity()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.entity.inc`](_file.md), lines 216–231 · [local source](../../../../../source/modules/field/tests/field_test.entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc#L216-L231)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function field_test_create_stub_entity($id = 1, $vid = 1, $bundle = 'test_bundle', $label = '')
```

## Documentation

```text
Creates a basic test_entity entity.
```

## Code

```php
function field_test_create_stub_entity($id = 1, $vid = 1, $bundle = 'test_bundle', $label = '') {
  $entity = new stdClass();
  // Only set id and vid properties if they don't come as NULL (creation form).
  if (isset($id)) {
    $entity->ftid = $id;
  }
  if (isset($vid)) {
    $entity->ftvid = $vid;
  }
  $entity->fttype = $bundle;

  $label = !empty($label) ? $label : $bundle . ' label';
  $entity->ftlabel = $label;

  return $entity;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.entity.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
