# HelpTestCase::setUp()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 35–43 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L35-L43)
- **Class:** [HelpTestCase](../HelpTestCase.md)
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
    parent::setUp('blog', 'poll');

    $this->getModuleList();

    // Create users.
    $this->big_user = $this->drupalCreateUser(array('access administration pages', 'view the administration theme', 'administer permissions'));
    $this->any_user = $this->drupalCreateUser(array());
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
