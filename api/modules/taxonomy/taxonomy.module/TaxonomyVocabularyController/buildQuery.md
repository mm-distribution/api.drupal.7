# TaxonomyVocabularyController::buildQuery()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.module`](../_file.md), lines 1293–1299 · [local source](../../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1293-L1299)
- **Class:** [TaxonomyVocabularyController](../TaxonomyVocabularyController.md)
- **Module/theme:** taxonomy

## Signature

```php
protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function buildQuery($ids, $conditions = array(), $revision_id = FALSE) {
    $query = parent::buildQuery($ids, $conditions, $revision_id);
    $query->addTag('translatable');
    $query->orderBy('base.weight');
    $query->orderBy('base.name');
    return $query;
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
