# FieldFormTestCase::testFieldFormSingle()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1663–1714 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1663-L1714)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormSingle()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFieldFormSingle() {
    $this->field = $this->field_single;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget is displayed');
    $this->assertNoField("{$this->field_name}[$langcode][1][value]", 'No extraneous widget is displayed');
    // TODO : check that the widget is populated with default value ?

    // Submit with invalid value (field-level validation).
    $edit = array("{$this->field_name}[$langcode][0][value]" => -1);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('%name does not accept the value -1.', array('%name' => $this->instance['label'])), 'Field validation fails with invalid input.');
    // TODO : check that the correct field is flagged for error.

    // Create an entity
    $value = mt_rand(1, 127);
    $edit = array("{$this->field_name}[$langcode][0][value]" => $value);
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created');
    $entity = field_test_entity_test_load($id);
    $this->assertEqual($entity->{$this->field_name}[$langcode][0]['value'], $value, 'Field value was saved');

    // Display edit form.
    $this->drupalGet('test-entity/manage/' . $id . '/edit');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", $value, 'Widget is displayed with the correct default value');
    $this->assertNoField("{$this->field_name}[$langcode][1][value]", 'No extraneous widget is displayed');

    // Update the entity.
    $value = mt_rand(1, 127);
    $edit = array("{$this->field_name}[$langcode][0][value]" => $value);
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('test_entity @id has been updated.', array('@id' => $id)), 'Entity was updated');
    $entity = field_test_entity_test_load($id);
    $this->assertEqual($entity->{$this->field_name}[$langcode][0]['value'], $value, 'Field value was updated');

    // Empty the field.
    $value = '';
    $edit = array("{$this->field_name}[$langcode][0][value]" => $value);
    $this->drupalPost('test-entity/manage/' . $id . '/edit', $edit, t('Save'));
    $this->assertRaw(t('test_entity @id has been updated.', array('@id' => $id)), 'Entity was updated');
    $entity = field_test_entity_test_load($id);
    $this->assertIdentical($entity->{$this->field_name}, array(), 'Field was emptied');

  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
