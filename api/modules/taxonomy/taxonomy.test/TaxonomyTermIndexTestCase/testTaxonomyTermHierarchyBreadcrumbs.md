# TaxonomyTermIndexTestCase::testTaxonomyTermHierarchyBreadcrumbs()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1383–1393 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1383-L1393)
- **Class:** [TaxonomyTermIndexTestCase](../TaxonomyTermIndexTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermHierarchyBreadcrumbs()
```

## Documentation

```text
Tests that there is a link to the parent term on the child term page.
```

## Code

```php
  function testTaxonomyTermHierarchyBreadcrumbs() {
    // Create two taxonomy terms and set term2 as the parent of term1.
    $term1 = $this->createTerm($this->vocabulary);
    $term2 = $this->createTerm($this->vocabulary);
    $term1->parent = array($term2->tid);
    taxonomy_term_save($term1);

    // Verify that the page breadcrumbs include a link to the parent term.
    $this->drupalGet('taxonomy/term/' . $term1->tid);
    $this->assertRaw(l($term2->name, 'taxonomy/term/' . $term2->tid), 'Parent term link is displayed when viewing the node.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
