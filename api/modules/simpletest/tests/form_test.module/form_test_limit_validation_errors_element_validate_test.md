# form_test_limit_validation_errors_element_validate_test()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 551–555 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L551-L555)
- **Module/theme:** batch_test

## Signature

```php
function form_test_limit_validation_errors_element_validate_test(&$element, &$form_state)
```

## Documentation

```text
Form element validation handler for the 'test' element.
```

## Code

```php
function form_test_limit_validation_errors_element_validate_test(&$element, &$form_state) {
  if ($element['#value'] == 'invalid') {
    form_error($element, t('@label element is invalid', array('@label' => $element['#title'])));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
