# FieldFormTestCase::testFieldFormUnlimited()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1755–1829 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1755-L1829)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormUnlimited()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFieldFormUnlimited() {
    $this->field = $this->field_unlimited;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Display creation form -> 1 widget.
    $this->drupalGet('test-entity/add/test-bundle');
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget 1 is displayed');
    $this->assertNoField("{$this->field_name}[$langcode][1][value]", 'No extraneous widget is displayed');

    // Press 'add more' button -> 2 widgets.
    $this->drupalPost(NULL, array(), t('Add another item'));
    $this->assertFieldByName("{$this->field_name}[$langcode][0][value]", '', 'Widget 1 is displayed');
    $this->assertFieldByName("{$this->field_name}[$langcode][1][value]", '', 'New widget is displayed');
    $this->assertNoField("{$this->field_name}[$langcode][2][value]", 'No extraneous widget is displayed');
    // TODO : check that non-field inpurs are preserved ('title')...

    // Yet another time so that we can play with more values -> 3 widgets.
    $this->drupalPost(NULL, array(), t('Add another item'));

    // Prepare values and weights.
    $count = 3;
    $delta_range = $count - 1;
    $values = $weights = $pattern = $expected_values = $edit = array();
    for ($delta = 0; $delta <= $delta_range; $delta++) {
      // Assign unique random values and weights.
      do {
        $value = mt_rand(1, 127);
      } while (in_array($value, $values));
      do {
        $weight = mt_rand(-$delta_range, $delta_range);
      } while (in_array($weight, $weights));
      $edit["$this->field_name[$langcode][$delta][value]"] = $value;
      $edit["$this->field_name[$langcode][$delta][_weight]"] = $weight;
      // We'll need three slightly different formats to check the values.
      $values[$delta] = $value;
      $weights[$delta] = $weight;
      $field_values[$weight]['value'] = (string) $value;
      $pattern[$weight] = "<input [^>]*value=\"$value\" [^>]*";
    }

    // Press 'add more' button -> 4 widgets
    $this->drupalPost(NULL, $edit, t('Add another item'));
    for ($delta = 0; $delta <= $delta_range; $delta++) {
      $this->assertFieldByName("$this->field_name[$langcode][$delta][value]", $values[$delta], "Widget $delta is displayed and has the right value");
      $this->assertFieldByName("$this->field_name[$langcode][$delta][_weight]", $weights[$delta], "Widget $delta has the right weight");
    }
    ksort($pattern);
    $pattern = implode('.*', array_values($pattern));
    $this->assertPattern("|$pattern|s", 'Widgets are displayed in the correct order');
    $this->assertFieldByName("$this->field_name[$langcode][$delta][value]", '', "New widget is displayed");
    $this->assertFieldByName("$this->field_name[$langcode][$delta][_weight]", $delta, "New widget has the right weight");
    $this->assertNoField("$this->field_name[$langcode][" . ($delta + 1) . '][value]', 'No extraneous widget is displayed');

    // Submit the form and create the entity.
    $this->drupalPost(NULL, $edit, t('Save'));
    preg_match('|test-entity/manage/(\d+)/edit|', $this->url, $match);
    $id = $match[1];
    $this->assertRaw(t('test_entity @id has been created.', array('@id' => $id)), 'Entity was created');
    $entity = field_test_entity_test_load($id);
    ksort($field_values);
    $field_values = array_values($field_values);
    $this->assertIdentical($entity->{$this->field_name}[$langcode], $field_values, 'Field values were saved in the correct order');

    // Display edit form: check that the expected number of widgets is
    // displayed, with correct values change values, reorder, leave an empty
    // value in the middle.
    // Submit: check that the entity is updated with correct values
    // Re-submit: check that the field can be emptied.

    // Test with several multiple fields in a form
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
