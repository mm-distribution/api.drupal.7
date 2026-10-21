# AJAXCommandsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 225–231 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L225-L231)
- **Class:** [AJAXCommandsTestCase](../AJAXCommandsTestCase.md)
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
      'name' => 'AJAX commands',
      'description' => 'Performs tests on AJAX framework commands.',
      'group' => 'AJAX',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
