# FormElementTestCase::testWeightDefaultValue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 598–606 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L598-L606)
- **Class:** [FormElementTestCase](../FormElementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testWeightDefaultValue()
```

## Documentation

```text
Tests Weight form element #default_value behavior.
```

## Code

```php
  public function testWeightDefaultValue() {
    $element = array(
      '#type' => 'weight',
      '#delta' => 10,
      '#default_value' => 15,
    );
    $element = form_process_weight($element);
    $this->assertTrue(isset($element['#options'][$element['#default_value']]), 'Default value exists in #options list');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
