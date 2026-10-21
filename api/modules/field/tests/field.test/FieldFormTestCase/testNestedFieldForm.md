# FieldFormTestCase::testNestedFieldForm()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2065–2169 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2065-L2169)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testNestedFieldForm()
```

## Documentation

```text
Tests Field API form integration within a subform.
```

## Code

```php
  function testNestedFieldForm() {
    // Add two instances on the 'test_bundle'
    field_create_field($this->field_single);
    field_create_field($this->field_unlimited);
    $this->instance['field_name'] = 'field_single';
    $this->instance['label'] = 'Single field';
    field_create_instance($this->instance);
    $this->instance['field_name'] = 'field_unlimited';
    $this->instance['label'] = 'Unlimited field';
    field_create_instance($this->instance);

    // Create two entities.
    $entity_1 = field_test_create_stub_entity(1, 1);
    $entity_1->is_new = TRUE;
    $entity_1->field_single[LANGUAGE_NONE][] = array('value' => 0);
    $entity_1->field_unlimited[LANGUAGE_NONE][] = array('value' => 1);
    field_test_entity_save($entity_1);

    $entity_2 = field_test_create_stub_entity(2, 2);
    $entity_2->is_new = TRUE;
    $entity_2->field_single[LANGUAGE_NONE][] = array('value' => 10);
    $entity_2->field_unlimited[LANGUAGE_NONE][] = array('value' => 11);
    field_test_entity_save($entity_2);

    // Display the 'combined form'.
    $this->drupalGet('test-entity/nested/1/2');
    $this->assertFieldByName('field_single[und][0][value]', 0, 'Entity 1: field_single value appears correctly is the form.');
    $this->assertFieldByName('field_unlimited[und][0][value]', 1, 'Entity 1: field_unlimited value 0 appears correctly is the form.');
    $this->assertFieldByName('entity_2[field_single][und][0][value]', 10, 'Entity 2: field_single value appears correctly is the form.');
    $this->assertFieldByName('entity_2[field_unlimited][und][0][value]', 11, 'Entity 2: field_unlimited value 0 appears correctly is the form.');

    // Submit the form and check that the entities are updated accordingly.
    $edit = array(
      'field_single[und][0][value]' => 1,
      'field_unlimited[und][0][value]' => 2,
      'field_unlimited[und][1][value]' => 3,
      'entity_2[field_single][und][0][value]' => 11,
      'entity_2[field_unlimited][und][0][value]' => 12,
      'entity_2[field_unlimited][und][1][value]' => 13,
    );
    $this->drupalPost(NULL, $edit, t('Save'));
    field_cache_clear();
    $entity_1 = field_test_create_stub_entity(1);
    $entity_2 = field_test_create_stub_entity(2);
    $this->assertFieldValues($entity_1, 'field_single', LANGUAGE_NONE, array(1));
    $this->assertFieldValues($entity_1, 'field_unlimited', LANGUAGE_NONE, array(2, 3));
    $this->assertFieldValues($entity_2, 'field_single', LANGUAGE_NONE, array(11));
    $this->assertFieldValues($entity_2, 'field_unlimited', LANGUAGE_NONE, array(12, 13));

    // Submit invalid values and check that errors are reported on the
    // correct widgets.
    $edit = array(
      'field_unlimited[und][1][value]' => -1,
    );
    $this->drupalPost('test-entity/nested/1/2', $edit, t('Save'));
    $this->assertRaw(t('%label does not accept the value -1', array('%label' => 'Unlimited field')), 'Entity 1: the field validation error was reported.');
    $error_field = $this->xpath('//input[@id=:id and contains(@class, "error")]', array(':id' => 'edit-field-unlimited-und-1-value'));
    $this->assertTrue($error_field, 'Entity 1: the error was flagged on the correct element.');
    $edit = array(
      'entity_2[field_unlimited][und][1][value]' => -1,
    );
    $this->drupalPost('test-entity/nested/1/2', $edit, t('Save'));
    $this->assertRaw(t('%label does not accept the value -1', array('%label' => 'Unlimited field')), 'Entity 2: the field validation error was reported.');
    $error_field = $this->xpath('//input[@id=:id and contains(@class, "error")]', array(':id' => 'edit-entity-2-field-unlimited-und-1-value'));
    $this->assertTrue($error_field, 'Entity 2: the error was flagged on the correct element.');

    // Test that reordering works on both entities.
    $edit = array(
      'field_unlimited[und][0][_weight]' => 0,
      'field_unlimited[und][1][_weight]' => -1,
      'entity_2[field_unlimited][und][0][_weight]' => 0,
      'entity_2[field_unlimited][und][1][_weight]' => -1,
    );
    $this->drupalPost('test-entity/nested/1/2', $edit, t('Save'));
    field_cache_clear();
    $this->assertFieldValues($entity_1, 'field_unlimited', LANGUAGE_NONE, array(3, 2));
    $this->assertFieldValues($entity_2, 'field_unlimited', LANGUAGE_NONE, array(13, 12));

    // Test the 'add more' buttons. Only Ajax submission is tested, because
    // the two 'add more' buttons present in the form have the same #value,
    // which confuses drupalPost().
    // 'Add more' button in the first entity:
    $this->drupalGet('test-entity/nested/1/2');
    $this->drupalPostAJAX(NULL, array(), 'field_unlimited_add_more');
    $this->assertFieldByName('field_unlimited[und][0][value]', 3, 'Entity 1: field_unlimited value 0 appears correctly is the form.');
    $this->assertFieldByName('field_unlimited[und][1][value]', 2, 'Entity 1: field_unlimited value 1 appears correctly is the form.');
    $this->assertFieldByName('field_unlimited[und][2][value]', '', 'Entity 1: field_unlimited value 2 appears correctly is the form.');
    $this->assertFieldByName('field_unlimited[und][3][value]', '', 'Entity 1: an empty widget was added for field_unlimited value 3.');
    // 'Add more' button in the first entity (changing field values):
    $edit = array(
      'entity_2[field_unlimited][und][0][value]' => 13,
      'entity_2[field_unlimited][und][1][value]' => 14,
      'entity_2[field_unlimited][und][2][value]' => 15,
    );
    $this->drupalPostAJAX(NULL, $edit, 'entity_2_field_unlimited_add_more');
    $this->assertFieldByName('entity_2[field_unlimited][und][0][value]', 13, 'Entity 2: field_unlimited value 0 appears correctly is the form.');
    $this->assertFieldByName('entity_2[field_unlimited][und][1][value]', 14, 'Entity 2: field_unlimited value 1 appears correctly is the form.');
    $this->assertFieldByName('entity_2[field_unlimited][und][2][value]', 15, 'Entity 2: field_unlimited value 2 appears correctly is the form.');
    $this->assertFieldByName('entity_2[field_unlimited][und][3][value]', '', 'Entity 2: an empty widget was added for field_unlimited value 3.');
    // Save the form and check values are saved correclty.
    $this->drupalPost(NULL, array(), t('Save'));
    field_cache_clear();
    $this->assertFieldValues($entity_1, 'field_unlimited', LANGUAGE_NONE, array(3, 2));
    $this->assertFieldValues($entity_2, 'field_unlimited', LANGUAGE_NONE, array(13, 14, 15));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
