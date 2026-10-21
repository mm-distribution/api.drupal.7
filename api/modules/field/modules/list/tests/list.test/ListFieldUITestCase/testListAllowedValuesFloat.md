# ListFieldUITestCase::testListAllowedValuesFloat()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 295–340 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L295-L340)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testListAllowedValuesFloat()
```

## Documentation

```text
List (float) : test 'allowed values' input.
```

## Code

```php
  function testListAllowedValuesFloat() {
    $this->field_name = 'field_list_float';
    $this->createListField('list_float');

    // Flat list of textual values.
    $string = "Zero\nOne";
    $array = array('0' => 'Zero', '1' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Unkeyed lists are accepted.');
    // Explicit numeric keys.
    $string = "0|Zero\n.5|Point five";
    $array = array('0' => 'Zero', '0.5' => 'Point five');
    $this->assertAllowedValuesInput($string, $array, 'Integer keys are accepted.');
    // Check that values can be added and removed.
    $string = "0|Zero\n.5|Point five\n1.0|One";
    $array = array('0' => 'Zero', '0.5' => 'Point five', '1' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added and removed.');
    // Non-numeric keys.
    $this->assertAllowedValuesInput("abc|abc\n", 'each key must be a valid integer or decimal', 'Non numeric keys are rejected.');
    // Mixed list of keyed and unkeyed values.
    $this->assertAllowedValuesInput("Zero\n1|One\n", 'invalid input', 'Mixed lists are rejected.');

    // Create a node with actual data for the field.
    $settings = array(
      'type' => $this->type,
      $this->field_name => array(LANGUAGE_NONE => array(array('value' => .5))),
    );
    $node = $this->drupalCreateNode($settings);

    // Check that a flat list of values is rejected once the field has data.
    $this->assertAllowedValuesInput("Zero\nOne", 'invalid input', 'Unkeyed lists are rejected once the field has data.');

    // Check that values can be added but values in use cannot be removed.
    $string = "0|Zero\n.5|Point five\n2|Two";
    $array = array('0' => 'Zero', '0.5' => 'Point five', '2' => 'Two');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added.');
    $string = "0|Zero\n.5|Point five";
    $array = array('0' => 'Zero', '0.5' => 'Point five');
    $this->assertAllowedValuesInput($string, $array, 'Values not in use can be removed.');
    $this->assertAllowedValuesInput("0|Zero", 'some values are being removed while currently in use', 'Values in use cannot be removed.');

    // Delete the node, remove the value.
    node_delete($node->nid);
    $string = "0|Zero";
    $array = array('0' => 'Zero');
    $this->assertAllowedValuesInput($string, $array, 'Values not in use can be removed.');
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
