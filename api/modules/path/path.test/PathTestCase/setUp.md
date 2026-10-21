# PathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 20–26 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L20-L26)
- **Class:** [PathTestCase](../PathTestCase.md)
- **Module/theme:** path

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('path');

    // Create test user and login.
    $web_user = $this->drupalCreateUser(array('create page content', 'edit own page content', 'administer url aliases', 'create url aliases', 'access content overview'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
