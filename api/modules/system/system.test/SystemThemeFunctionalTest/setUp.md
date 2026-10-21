# SystemThemeFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1910–1916 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1910-L1916)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    $this->admin_user = $this->drupalCreateUser(array('access administration pages', 'view the administration theme', 'administer themes', 'bypass node access', 'administer blocks'));
    $this->drupalLogin($this->admin_user);
    $this->node = $this->drupalCreateNode();
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
