# FilterHooksTestCase::setUp()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1940–1944 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1940-L1944)
- **Class:** [FilterHooksTestCase](../FilterHooksTestCase.md)
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
    parent::setUp('block', 'filter_test');
    $admin_user = $this->drupalCreateUser(array('administer filters', 'administer blocks'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
