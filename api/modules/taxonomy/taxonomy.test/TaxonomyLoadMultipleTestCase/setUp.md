# TaxonomyLoadMultipleTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1411–1415 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1411-L1415)
- **Class:** [TaxonomyLoadMultipleTestCase](../TaxonomyLoadMultipleTestCase.md)
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
    parent::setUp();
    $this->taxonomy_admin = $this->drupalCreateUser(array('administer taxonomy'));
    $this->drupalLogin($this->taxonomy_admin);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
