# FieldFormTestCase::testFieldFormMultivalueWithRequiredRadio()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1855–1895 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1855-L1895)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormMultivalueWithRequiredRadio()
```

## Documentation

```text
Tests widget handling of multiple required radios.
```

## Code

```php
  function testFieldFormMultivalueWithRequiredRadio() {
    // Create a multivalue test field.
    $this->field = $this->field_unlimited;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Add a required radio field.
    field_create_field(array(
      'field_name' => 'required_radio_test',
      'type' => 'list_text',
      'settings' => array(
        'allowed_values' => array('yes' => 'yes', 'no' => 'no'),
      ),
    ));
    field_create_instance(array(
      'field_name' => 'required_radio_test',
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'required' => TRUE,
      'widget' => array(
        'type' => 'options_buttons',
      ),
    ));

    // Display creation form.
    $this->drupalGet('test-entity/add/test-bundle');

    // Press the 'Add more' button.
    $this->drupalPost(NULL, array(), t('Add another item'));

    // Verify that no error is thrown by the radio element.
    $this->assertNoFieldByXpath('//div[contains(@class, "error")]', FALSE, 'No error message is displayed.');

    // Verify that the widget is added.
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget 1 is displayed');
    $this->assertFieldByName("{$this->field_name}[$langcode][1][value]", '', 'New widget is displayed');
    $this->assertNoField("{$this->field_name}[$langcode][2][value]", 'No extraneous widget is displayed');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
