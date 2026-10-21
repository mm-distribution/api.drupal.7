# NumberFieldTestCase::testNumberDecimalField()

- **Type:** Method
- **File:** [`modules/field/modules/number/number.test`](../_file.md), lines 33–117 · [local source](../../../../../../../source/modules/field/modules/number/number.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test#L33-L117)
- **Class:** [NumberFieldTestCase](../NumberFieldTestCase.md)
- **Module/theme:** number

## Signature

```php
function testNumberDecimalField()
```

## Documentation

```text
Test number_decimal field.
```

## Code

```php
  function testNumberDecimalField() {
    // Create a field with settings to validate.
    $this->field = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'number_decimal',
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

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');
    $langcode = LANGUAGE_NONE;
    $this->assertFieldByName("{$this->field['field_name']}[$langcode][0][value]", '', 'Widget is displayed');

    // Submit a signed decimal value within the allowed precision and scale.
    $value = '-1234.5678';
    $edit = array(
      "{$this->field['field_name']}[$langcode][0][value]" => $value,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created');
    $this->assertRaw($value, 'Value is displayed.');

    // Try to create entries with more than one decimal separator; assert fail.
    $wrong_entries = array(
      '3.14.159',
      '0..45469',
      '..4589',
      '6.459.52',
      '6.3..25',
    );

    foreach ($wrong_entries as $wrong_entry) {
      $this->drupalGet('test-entity/add/test-bundle');
      $edit = array(
        "{$this->field['field_name']}[$langcode][0][value]" => $wrong_entry,
      );
      $this->drupalPost(NULL, $edit, t('Save'));
      $this->assertText(
        t('There should only be one decimal separator (@separator)',
          array('@separator' => $this->field['settings']['decimal_separator'])),
        'Correctly failed to save decimal value with more than one decimal point.'
      );
    }

    // Try to create entries with minus sign not in the first position.
    $wrong_entries = array(
      '3-3',
      '4-',
      '1.3-',
      '1.2-4',
      '-10-10',
    );

    foreach ($wrong_entries as $wrong_entry) {
      $this->drupalGet('test-entity/add/test-bundle');
      $edit = array(
        "{$this->field['field_name']}[$langcode][0][value]" => $wrong_entry,
      );
      $this->drupalPost(NULL, $edit, t('Save'));
      $this->assertText(
        t('Only numbers and the decimal separator (@separator) allowed in ',
          array('@separator' => $this->field['settings']['decimal_separator'])),
        'Correctly failed to save decimal value with minus sign in the wrong position.'
      );
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/number/number.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test) · Licensed GPL-2.0-or-later (see LICENSE)._
