# FormElementTestCase::testOptions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 557–593 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L557-L593)
- **Class:** [FormElementTestCase](../FormElementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testOptions()
```

## Documentation

```text
Tests expansion of #options for #type checkboxes and radios.
```

## Code

```php
  function testOptions() {
    $this->drupalGet('form-test/checkboxes-radios');

    // Verify that all options appear in their defined order.
    foreach (array('checkbox', 'radio') as $type) {
      $elements = $this->xpath('//input[@type=:type]', array(':type' => $type));
      $expected_values = array('0', 'foo', '1', 'bar', '>');
      foreach ($elements as $element) {
        $expected = array_shift($expected_values);
        $this->assertIdentical((string) $element['value'], $expected);
      }
    }

    // Enable customized option sub-elements.
    $this->drupalGet('form-test/checkboxes-radios/customize');

    // Verify that all options appear in their defined order, taking a custom
    // #weight into account.
    foreach (array('checkbox', 'radio') as $type) {
      $elements = $this->xpath('//input[@type=:type]', array(':type' => $type));
      $expected_values = array('0', 'foo', 'bar', '>', '1');
      foreach ($elements as $element) {
        $expected = array_shift($expected_values);
        $this->assertIdentical((string) $element['value'], $expected);
      }
    }
    // Verify that custom #description properties are output.
    foreach (array('checkboxes', 'radios') as $type) {
      $elements = $this->xpath('//input[@id=:id]/following-sibling::div[@class=:class]', array(
        ':id' => 'edit-' . $type . '-foo',
        ':class' => 'description',
      ));
      $this->assertTrue(count($elements), format_string('Custom %type option description found.', array(
        '%type' => $type,
      )));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
