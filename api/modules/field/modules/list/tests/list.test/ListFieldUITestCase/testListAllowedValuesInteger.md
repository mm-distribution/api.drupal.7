# ListFieldUITestCase::testListAllowedValuesInteger()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 244–290 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L244-L290)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testListAllowedValuesInteger()
```

## Documentation

```text
List (integer) : test 'allowed values' input.
```

## Code

```php
  function testListAllowedValuesInteger() {
    $this->field_name = 'field_list_integer';
    $this->createListField('list_integer');

    // Flat list of textual values.
    $string = "Zero\nOne";
    $array = array('0' => 'Zero', '1' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Unkeyed lists are accepted.');
    // Explicit integer keys.
    $string = "0|Zero\n2|Two";
    $array = array('0' => 'Zero', '2' => 'Two');
    $this->assertAllowedValuesInput($string, $array, 'Integer keys are accepted.');
    // Check that values can be added and removed.
    $string = "0|Zero\n1|One";
    $array = array('0' => 'Zero', '1' => 'One');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added and removed.');
    // Non-integer keys.
    $this->assertAllowedValuesInput("1.1|One", 'keys must be integers', 'Non integer keys are rejected.');
    $this->assertAllowedValuesInput("abc|abc", 'keys must be integers', 'Non integer keys are rejected.');
    // Mixed list of keyed and unkeyed values.
    $this->assertAllowedValuesInput("Zero\n1|One", 'invalid input', 'Mixed lists are rejected.');

    // Create a node with actual data for the field.
    $settings = array(
      'type' => $this->type,
      $this->field_name => array(LANGUAGE_NONE => array(array('value' => 1))),
    );
    $node = $this->drupalCreateNode($settings);

    // Check that a flat list of values is rejected once the field has data.
    $this->assertAllowedValuesInput( "Zero\nOne", 'invalid input', 'Unkeyed lists are rejected once the field has data.');

    // Check that values can be added but values in use cannot be removed.
    $string = "0|Zero\n1|One\n2|Two";
    $array = array('0' => 'Zero', '1' => 'One', '2' => 'Two');
    $this->assertAllowedValuesInput($string, $array, 'Values can be added.');
    $string = "0|Zero\n1|One";
    $array = array('0' => 'Zero', '1' => 'One');
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
