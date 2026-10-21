# NoHelpTestCase::setUp()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 127–131 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L127-L131)
- **Class:** [NoHelpTestCase](../NoHelpTestCase.md)
- **Module/theme:** help

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Use one of the test modules that do not implement hook_help().
    parent::setUp('menu_test');
    $this->big_user = $this->drupalCreateUser(array('access administration pages'));
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
