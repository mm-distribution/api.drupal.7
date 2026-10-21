# DrupalMatchPathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 24–33 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L24-L33)
- **Class:** [DrupalMatchPathTestCase](../DrupalMatchPathTestCase.md)
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
    // Set up the database and testing environment.
    parent::setUp();

    // Set up a random site front page to test the '<front>' placeholder.
    $this->front = $this->randomName();
    variable_set('site_frontpage', $this->front);
    // Refresh our static variables from the database.
    $this->refreshVariables();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
