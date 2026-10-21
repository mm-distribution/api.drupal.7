# FormsTestCase::assertFormValuesDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 380–400 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L380-L400)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertFormValuesDefault($values, $form)
```

## Documentation

```text
Assert that the values submitted to a form matches the default values of the elements.
```

## Code

```php
  function assertFormValuesDefault($values, $form) {
    foreach (element_children($form) as $key) {
      if (isset($form[$key]['#default_value'])) {
        if (isset($form[$key]['#expected_value'])) {
          $expected_value = $form[$key]['#expected_value'];
        }
        else {
          $expected_value = $form[$key]['#default_value'];
        }

        if ($key == 'checkboxes_multiple') {
          // Checkboxes values are not filtered out.
          $values[$key] = array_filter($values[$key]);
        }
        $this->assertIdentical($expected_value, $values[$key], format_string('Default value for %type: expected %expected, returned %returned.', array('%type' => $key, '%expected' => var_export($expected_value, TRUE), '%returned' => var_export($values[$key], TRUE))));
      }

      // Recurse children.
      $this->assertFormValuesDefault($values, $form[$key]);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
