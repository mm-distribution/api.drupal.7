# FilterSecurityTestCase::setUp()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 847–851 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L847-L851)
- **Class:** [FilterSecurityTestCase](../FilterSecurityTestCase.md)
- **Module/theme:** filter

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('php', 'filter_test');
    $this->admin_user = $this->drupalCreateUser(array('administer modules', 'administer filters', 'administer site configuration'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
