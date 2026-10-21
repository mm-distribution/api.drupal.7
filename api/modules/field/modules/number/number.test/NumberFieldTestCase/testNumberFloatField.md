# NumberFieldTestCase::testNumberFloatField()

- **Type:** Method
- **File:** [`modules/field/modules/number/number.test`](../_file.md), lines 159–199 · [local source](../../../../../../../source/modules/field/modules/number/number.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test#L159-L199)
- **Class:** [NumberFieldTestCase](../NumberFieldTestCase.md)
- **Module/theme:** number

## Signature

```php
function testNumberFloatField()
```

## Documentation

```text
Test number_float field.
```

## Code

```php
  function testNumberFloatField() {
    $this->field = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'number_float',
      'settings' => array(
        'precision' => 8, 'scale' => 4, 'decimal_separator' => '.',
      )
    );
    field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field['field_name'],
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'number',
      ),
      'display' => array(
        'default' => array(
          'type' => 'number_decimal',
        ),
      ),
    );
    field_create_instance($this->instance);

    $langcode = LANGUAGE_NONE;
    $value = array(
      '9.' => '9',
      '.' => '0',
      '123.55' => '123.55',
      '.55' => '0.55',
      '-0.55' => '-0.55',
    );
    foreach($value as $key => $value) {
      $edit = array(
        "{$this->field['field_name']}[$langcode][0][value]" => $key,
      );
      $this->drupalPost('test-entity/add/test-bundle', $edit, t('Save'));
      $this->assertNoText("PDOException");
      $this->assertRaw($value, 'Correct value is displayed.');
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/number/number.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test) · Licensed GPL-2.0-or-later (see LICENSE)._
