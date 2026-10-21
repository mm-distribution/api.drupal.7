# FieldFormTestCase::testFieldFormMultipleWidget()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1954–1989 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1954-L1989)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormMultipleWidget()
```

## Documentation

```text
Tests widgets handling multiple values.
```

## Code

```php
  function testFieldFormMultipleWidget() {
    // Create a field with fixed cardinality and an instance using a multiple
    // widget.
    $this->field = $this->field_multiple;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    $this->instance['widget']['type'] = 'test_field_widget_multiple';
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode]", '', 'Widget is displayed.');

    // Create entity with three values.
    $edit = array("{$this->field_name}[$langcode]" => '1, 2, 3');
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];

    // Check that the values were saved.
    $entity_init = field_test_create_stub_entity($id);
    $this->assertFieldValues($entity_init, $this->field_name, $langcode, array(1, 2, 3));

    // Display the form, check that the values are correctly filled in.
    $this->drupalGet('test-entity/manage/' . $id . '/edit');
    $this->assertFieldByName("{$this->field_name}[$langcode]", '1, 2, 3', 'Widget is displayed.');

    // Submit the form with more values than the field accepts.
    $edit = array("{$this->field_name}[$langcode]" => '1, 2, 3, 4, 5');
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw('this field cannot hold more than 4 values', 'Form validation failed.');
    // Check that the field values were not submitted.
    $this->assertFieldValues($entity_init, $this->field_name, $langcode, array(1, 2, 3));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
