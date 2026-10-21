# TaxonomyQueryAlterTestCase::setupQueryTagTestHooks()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2198–2203 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2198-L2203)
- **Class:** [TaxonomyQueryAlterTestCase](../TaxonomyQueryAlterTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
protected function setupQueryTagTestHooks()
```

## Documentation

```text
Sets up the hooks in the test module.
```

## Code

```php
  protected function setupQueryTagTestHooks() {
    taxonomy_terms_static_reset();
    variable_set('taxonomy_test_query_alter', 0);
    variable_set('taxonomy_test_query_term_access_alter', 0);
    variable_set('taxonomy_test_query_taxonomy_term_access_alter', 0);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
