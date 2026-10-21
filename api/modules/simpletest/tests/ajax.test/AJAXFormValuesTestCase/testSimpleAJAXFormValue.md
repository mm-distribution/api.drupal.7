# AJAXFormValuesTestCase::testSimpleAJAXFormValue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 406–432 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L406-L432)
- **Class:** [AJAXFormValuesTestCase](../AJAXFormValuesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleAJAXFormValue()
```

## Documentation

```text
Create a simple form, then POST to system/ajax to change to it.
```

## Code

```php
  function testSimpleAJAXFormValue() {
    // Verify form values of a select element.
    foreach (array('red', 'green', 'blue') as $item) {
      $edit = array(
        'select' => $item,
      );
      $commands = $this->drupalPostAJAX('ajax_forms_test_get_form', $edit, 'select');
      $expected = array(
        'command' => 'data',
        'value' => $item,
      );
      $this->assertCommand($commands, $expected, "verification of AJAX form values from a selectbox issued with a correct value");
    }

    // Verify form values of a checkbox element.
    foreach (array(FALSE, TRUE) as $item) {
      $edit = array(
        'checkbox' => $item,
      );
      $commands = $this->drupalPostAJAX('ajax_forms_test_get_form', $edit, 'checkbox');
      $expected = array(
        'command' => 'data',
        'value' => (int) $item,
      );
      $this->assertCommand($commands, $expected, "verification of AJAX form values from a checkbox issued with a correct value");
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
