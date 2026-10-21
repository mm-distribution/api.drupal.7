# TaxonomyTermCacheUsageTestCase::testTaxonomyGetTermByNameCacheUsage()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2240–2256 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2240-L2256)
- **Class:** [TaxonomyTermCacheUsageTestCase](../TaxonomyTermCacheUsageTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyGetTermByNameCacheUsage()
```

## Documentation

```text
Test taxonomy_get_term_by_name() cache usage.
```

## Code

```php
  function testTaxonomyGetTermByNameCacheUsage() {
    // Create vocabulary and term.
    $new_vocabulary = $this->createVocabulary();
    $new_term = new stdClass();
    $new_term->name = 'MixedCaseTerm';
    $new_term->vid = $new_vocabulary->vid;
    taxonomy_term_save($new_term);

    // Try to load term with mixed case letters from the cache.
    $taxonomy_controller = new TestTaxonomyTermController('taxonomy_term');
    // First load to warm the cache.
    $terms = $taxonomy_controller->load(array(), array('name' => $new_term->name));
    $this->assertTrue(isset($terms[$new_term->tid]), 'Term loaded using exact name and vocabulary machine name.');
    // Second load should load the $new_term from the cache.
    $terms = $taxonomy_controller->loadFromCache(array(), array('name' => $new_term->name));
    $this->assertTrue(isset($terms[$new_term->tid]), 'Term loaded using the cache.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
