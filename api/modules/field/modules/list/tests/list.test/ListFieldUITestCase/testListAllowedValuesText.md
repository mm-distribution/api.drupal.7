# ListFieldUITestCase::testListAllowedValuesText()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 345–395 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L345-L395)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testListAllowedValuesText()
```

## Documentation

```text
List (text) : test 'allowed values' input.
```

## Code

```php
  function testListAllowedValuesText() {
    $this->field_name = 'field_list_text';
    $this->createListField('list_text');

    // Flat list of textual values.
    $string = "Zero\nOne";
    $array = array('Zero' => 'Zero', 'One' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Unkeyed lists are accepted.');
    // Explicit keys.
    $string = "zero|Zero\none|One";
    $array = array('zero' => 'Zero', 'one' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Explicit keys are accepted.');
    // Check that values can be added and removed.
    $string = "zero|Zero\ntwo|Two";
    $array = array('zero' => 'Zero', 'two' => 'Two');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added and removed.');
    // Mixed list of keyed and unkeyed values.
    $string = "zero|Zero\nOne\n";
    $array = array('zero' => 'Zero', 'One' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Mixed lists are accepted.');
    // Overly long keys.
    $this->assertAllowedValuesInput("zero|Zero\n" . $this->randomName(256) . "|One", 'each key must be a string at most 255 characters long', 'Overly long keys are rejected.');

    // Create a node with actual data for the field.
    $settings = array(
      'type' => $this->type,
      $this->field_name => array(LANGUAGE_NONE => array(array('value' => 'One'))),
    );
    $node = $this->drupalCreateNode($settings);

    // Check that flat lists of values are still accepted once the field has
    // data.
    $string = "Zero\nOne";
    $array = array('Zero' => 'Zero', 'One' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Unkeyed lists are still accepted once the field has data.');

    // Check that values can be added but values in use cannot be removed.
    $string = "Zero\nOne\nTwo";
    $array = array('Zero' => 'Zero', 'One' => 'One', 'Two' => 'Two');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added.');
    $string = "Zero\nOne";
    $array = array('Zero' => 'Zero', 'One' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Values not in use can be removed.');
    $this->assertAllowedValuesInput("Zero", 'some values are being removed while currently in use', 'Values in use cannot be removed.');

    // Delete the node, remove the value.
    node_delete($node->nid);
    $string = "Zero";
    $array = array('Zero' => 'Zero');
    $this->assertAllowedValuesInput($string, $array, 'Values not in use can be removed.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
