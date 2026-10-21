# FormStateValuesCleanTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1632–1638 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1632-L1638)
- **Class:** [FormStateValuesCleanTestCase](../FormStateValuesCleanTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Form state values clearance',
      'description' => 'Test proper removal of submitted form values using form_state_values_clean().',
      'group' => 'Form API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
