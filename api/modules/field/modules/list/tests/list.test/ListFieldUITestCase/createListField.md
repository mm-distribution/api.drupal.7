# ListFieldUITestCase::createListField()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 445–463 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L445-L463)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
protected function createListField($type, $settings = array())
```

## Documentation

```text
Helper function to create list field of a given type.

@param string $type
  'list_integer', 'list_float', 'list_text' or 'list_boolean'
@param array $settings

@throws \FieldException
```

## Code

```php
  protected function createListField($type, $settings = array()) {
    // Create a test field and instance.
    $field = array(
      'field_name' => $this->field_name,
      'type' => $type,
    );
    if (!empty($settings)) {
      $field['settings'] = $settings;
    }
    field_create_field($field);
    $instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'node',
      'bundle' => $this->type,
    );
    field_create_instance($instance);

    $this->admin_path = 'admin/structure/types/manage/' . $this->hyphen_type . '/fields/' . $this->field_name;
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
