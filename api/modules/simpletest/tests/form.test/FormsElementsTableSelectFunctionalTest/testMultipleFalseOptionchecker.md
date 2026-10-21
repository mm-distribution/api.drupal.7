# FormsElementsTableSelectFunctionalTest::testMultipleFalseOptionchecker()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1110–1128 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1110-L1128)
- **Class:** [FormsElementsTableSelectFunctionalTest](../FormsElementsTableSelectFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultipleFalseOptionchecker()
```

## Documentation

```text
Test the whether the option checker gives an error on invalid tableselect values for radios.
```

## Code

```php
  function testMultipleFalseOptionchecker() {

    list($header, $options) = _form_test_tableselect_get_data();

    $form['tableselect'] = array(
      '#type' => 'tableselect',
      '#header' => $header,
      '#options' => $options,
      '#multiple' => FALSE,
    );

    // Test with a valid value.
    list($processed_form, $form_state, $errors) = $this->formSubmitHelper($form, array('tableselect' => 'row1'));
    $this->assertFalse(isset($errors['tableselect']), 'Option checker allows valid values for radio buttons.');

    // Test with an invalid value.
    list($processed_form, $form_state, $errors) = $this->formSubmitHelper($form, array('tableselect' => 'non_existing_value'));
    $this->assertTrue(isset($errors['tableselect']), 'Option checker disallows invalid values for radio buttons.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
