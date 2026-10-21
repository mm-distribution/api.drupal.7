# SessionHttpsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 554–560 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L554-L560)
- **Class:** [SessionHttpsTestCase](../SessionHttpsTestCase.md)
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
      'name' => 'Session HTTPS handling',
      'description' => 'Ensure that when running under HTTPS two session cookies are generated.',
      'group' => 'Session'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
