# DBLogTestCase::setUp()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 38–43 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L38-L43)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
function setUp()
```

## Documentation

```text
Enable modules and create users with specific permissions.
```

## Code

```php
  function setUp() {
    parent::setUp('dblog', 'blog', 'poll');
    // Create users.
    $this->big_user = $this->drupalCreateUser(array('administer site configuration', 'access administration pages', 'access site reports', 'administer users'));
    $this->any_user = $this->drupalCreateUser(array());
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
