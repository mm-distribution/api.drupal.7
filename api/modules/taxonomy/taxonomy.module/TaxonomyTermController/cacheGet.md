# TaxonomyTermController::cacheGet()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.module`](../_file.md), lines 1271–1282 · [local source](../../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1271-L1282)
- **Class:** [TaxonomyTermController](../TaxonomyTermController.md)
- **Module/theme:** taxonomy

## Signature

```php
protected function cacheGet($ids, $conditions = array())
```

## Documentation

_No docblock in source._

## Code

```php
  protected function cacheGet($ids, $conditions = array()) {
    $terms = parent::cacheGet($ids, $conditions);
    // Name matching is case insensitive, note that with some collations
    // LOWER() and drupal_strtolower() may return different results.
    foreach ($terms as $term) {
      $term_values = (array) $term;
      if (isset($conditions['name']) && drupal_strtolower($conditions['name']) != drupal_strtolower($term_values['name'])) {
        unset($terms[$term->tid]);
      }
    }
    return $terms;
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
