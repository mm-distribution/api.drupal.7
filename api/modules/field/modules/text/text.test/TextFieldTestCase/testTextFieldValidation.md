# TextFieldTestCase::testTextFieldValidation()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 36–74 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L36-L74)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

## Signature

```php
function testTextFieldValidation()
```

## Documentation

```text
Test text field validation.
```

## Code

```php
  function testTextFieldValidation() {
    // Create a field with settings to validate.
    $max_length = 3;
    $this->field = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'text',
      'settings' => array(
        'max_length' => $max_length,
      )
    );
    field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'text_textfield',
      ),
      'display' => array(
        'default' => array(
          'type' => 'text_default',
        ),
      ),
    );
    field_create_instance($this->instance);
    // Test valid and invalid values with field_attach_validate().
    $entity = field_test_create_stub_entity();
    $langcode = LANGUAGE_NONE;
    for ($i = 0; $i <= $max_length + 2; $i++) {
      $entity->{$this->field['field_name']}[$langcode][0]['value'] = str_repeat('x', $i);
      try {
        field_attach_validate('test_entity', $entity);
        $this->assertTrue($i <= $max_length, "Length $i does not cause validation error when max_length is $max_length");
      }
      catch (FieldValidationException $e) {
        $this->assertTrue($i > $max_length, "Length $i causes validation error when max_length is $max_length");
      }
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
