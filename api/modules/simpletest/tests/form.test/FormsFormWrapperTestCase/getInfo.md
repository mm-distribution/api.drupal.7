# FormsFormWrapperTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1606–1612 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1606-L1612)
- **Class:** [FormsFormWrapperTestCase](../FormsFormWrapperTestCase.md)
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
      'name' => 'Form wrapper callback',
      'description' => 'Tests form wrapper callbacks to pass a prebuilt form to form builder functions.',
      'group' => 'Form API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
