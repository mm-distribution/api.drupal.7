# FieldFormTestCase::testFieldFormSingleRequired()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1716–1745 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1716-L1745)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormSingleRequired()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFieldFormSingleRequired() {
    $this->field = $this->field_single;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    $this->instance['required'] = TRUE;
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Submit with missing required value.
    $edit = array();
    $this->drupalPost('test-entity/add/test-bundle', $edit, t('Save'));
    $this->assertRaw(t('!name field is required.', array('!name' => $this->instance['label'])), 'Required field with no value fails validation');

    // Create an entity
    $value = mt_rand(1, 127);
    $edit = array("{$this->field_name}[$langcode][0][value]" => $value);
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created');
    $entity = field_test_entity_test_load($id);
    $this->assertEqual($entity->{$this->field_name}[$langcode][0]['value'], $value, 'Field value was saved');

    // Edit with missing required value.
    $value = '';
    $edit = array("{$this->field_name}[$langcode][0][value]" => $value);
    $this->drupalPost('test-entity/manage/' . $id . '/edit', $edit, t('Save'));
    $this->assertRaw(t('!name field is required.', array('!name' => $this->instance['label'])), 'Required field with no value fails validation');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
