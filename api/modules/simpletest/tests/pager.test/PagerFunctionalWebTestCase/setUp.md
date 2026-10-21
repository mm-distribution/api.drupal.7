# PagerFunctionalWebTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/pager.test`](../_file.md), lines 23–35 · [local source](../../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L23-L35)
- **Class:** [PagerFunctionalWebTestCase](../PagerFunctionalWebTestCase.md)
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
    parent::setUp(array('dblog'));

    // Insert 300 log messages.
    for ($i = 0; $i < 300; $i++) {
      watchdog('pager_test', $this->randomString(), NULL, WATCHDOG_DEBUG);
    }

    $this->admin_user = $this->drupalCreateUser(array(
      'access site reports',
    ));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._
