# FieldFormTestCase::testFieldFormJSAddMore()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1897–1949 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1897-L1949)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldFormJSAddMore()
```

## Documentation

_No docblock in source._

## Code

```php
  function testFieldFormJSAddMore() {
    $this->field = $this->field_unlimited;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    field_create_field($this->field);
    field_create_instance($this->instance);
    $langcode = LANGUAGE_NONE;

    // Display creation form -> 1 widget.
    $this->drupalGet('test-entity/add/test-bundle');

    // Press 'add more' button a couple times -> 3 widgets.
    // drupalPostAJAX() will not work iteratively, so we add those through
    // non-JS submission.
    $this->drupalPost(NULL, array(), t('Add another item'));
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
    // Press 'add more' button through Ajax, and place the expected HTML result
    // as the tested content.
    $commands = $this->drupalPostAJAX(NULL, $edit, $this->field_name . '_add_more');
    $this->content = $commands[1]['data'];

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
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
