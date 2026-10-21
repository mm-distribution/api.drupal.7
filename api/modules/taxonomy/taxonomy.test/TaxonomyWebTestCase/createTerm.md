# TaxonomyWebTestCase::createTerm()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 32–41 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L32-L41)
- **Class:** [TaxonomyWebTestCase](../TaxonomyWebTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function createTerm($vocabulary)
```

## Documentation

```text
Returns a new term with random properties in vocabulary $vid.
```

## Code

```php
  function createTerm($vocabulary) {
    $term = new stdClass();
    $term->name = $this->randomName();
    $term->description = $this->randomName();
    // Use the first available text format.
    $term->format = db_query_range('SELECT format FROM {filter_format}', 0, 1)->fetchField();
    $term->vid = $vocabulary->vid;
    taxonomy_term_save($term);
    return $term;
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
