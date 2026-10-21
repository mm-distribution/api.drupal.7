# SessionUnitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 850–856 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L850-L856)
- **Class:** [SessionUnitTestCase](../SessionUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Session unit tests',
      'description' => 'Test session handling functionality.',
      'group' => 'Session',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
