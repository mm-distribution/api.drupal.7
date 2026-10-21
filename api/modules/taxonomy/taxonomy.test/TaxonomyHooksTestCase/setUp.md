# TaxonomyHooksTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1477–1482 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1477-L1482)
- **Class:** [TaxonomyHooksTestCase](../TaxonomyHooksTestCase.md)
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
    parent::setUp('taxonomy', 'taxonomy_test');
    module_load_include('inc', 'taxonomy', 'taxonomy.pages');
    $taxonomy_admin = $this->drupalCreateUser(array('administer taxonomy'));
    $this->drupalLogin($taxonomy_admin);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
