# TaxonomyLegacyTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 503–507 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L503-L507)
- **Class:** [TaxonomyLegacyTestCase](../TaxonomyLegacyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('taxonomy');
    $this->admin_user = $this->drupalCreateUser(array('administer taxonomy', 'administer nodes', 'bypass node access'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
