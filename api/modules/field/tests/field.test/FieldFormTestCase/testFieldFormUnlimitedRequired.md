# FieldFormTestCase::testFieldFormUnlimitedRequired()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 1834–1850 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L1834-L1850)
- **Class:** [FieldFormTestCase](../FieldFormTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
public function testFieldFormUnlimitedRequired()
```

## Documentation

```text
Tests the position of the required label.
```

## Code

```php
  public function testFieldFormUnlimitedRequired() {
    $this->field = $this->field_unlimited;
    $this->field_name = $this->field['field_name'];
    $this->instance['field_name'] = $this->field_name;
    $this->instance['required'] = TRUE;
    field_create_field($this->field);
    field_create_instance($this->instance);

    // Display creation form -> 1 widget.
    $this->drupalGet('test-entity/add/test-bundle');
    $result = $this->xpath("//label[not(contains(@class, 'element-invisible')) and contains(text(), :label)]/span/text()", array(':label' => $this->instance['label']));
    $this->assertEqual($result[0], '*', 'Required symbol added to field label.');
    // Check that the label of the field input is visually hidden and contains
    // the field title and an indication of the delta for a11y.
    $result = $this->xpath("//label[contains(@class, 'element-invisible') and contains(text(), :label)]/span/text()", array(':label' => $this->instance['label']));
    $this->assertEqual($result[0], '*', 'Required symbol and field label are visually hidden.');
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
