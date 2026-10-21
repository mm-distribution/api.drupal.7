# SimpleTestFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 48–59 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L48-L59)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    if (!$this->inCURL()) {
      parent::setUp('simpletest');

      // Create and login user
      $admin_user = $this->drupalCreateUser(array('administer unit tests'));
      $this->drupalLogin($admin_user);
    }
    else {
      parent::setUp('non_existent_module');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
