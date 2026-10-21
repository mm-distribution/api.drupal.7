# ThemeFastTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 444–447 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L444-L447)
- **Class:** [ThemeFastTestCase](../ThemeFastTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('theme_test');
    $this->account = $this->drupalCreateUser(array('access user profiles'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
