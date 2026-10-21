# TaxonomyTermTestCase::testTaxonomyTermHierarchy()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 584–616 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L584-L616)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermHierarchy()
```

## Documentation

```text
Test terms in a single and multiple hierarchy.
```

## Code

```php
  function testTaxonomyTermHierarchy() {
    // Create two taxonomy terms.
    $term1 = $this->createTerm($this->vocabulary);
    $term2 = $this->createTerm($this->vocabulary);

    // Check that hierarchy is flat.
    $vocabulary = taxonomy_vocabulary_load($this->vocabulary->vid);
    $this->assertEqual(0, $vocabulary->hierarchy, 'Vocabulary is flat.');

    // Edit $term2, setting $term1 as parent.
    $edit = array();
    $edit['parent[]'] = array($term1->tid);
    $this->drupalPost('taxonomy/term/' . $term2->tid . '/edit', $edit, t('Save'));

    // Check the hierarchy.
    $children = taxonomy_get_children($term1->tid);
    $parents = taxonomy_get_parents($term2->tid);
    $this->assertTrue(isset($children[$term2->tid]), 'Child found correctly.');
    $this->assertTrue(isset($parents[$term1->tid]), 'Parent found correctly.');

    // Load and save a term, confirming that parents are still set.
    $term = taxonomy_term_load($term2->tid);
    taxonomy_term_save($term);
    $parents = taxonomy_get_parents($term2->tid);
    $this->assertTrue(isset($parents[$term1->tid]), 'Parent found correctly.');

    // Create a third term and save this as a parent of term2.
    $term3 = $this->createTerm($this->vocabulary);
    $term2->parent = array($term1->tid, $term3->tid);
    taxonomy_term_save($term2);
    $parents = taxonomy_get_parents($term2->tid);
    $this->assertTrue(isset($parents[$term1->tid]) && isset($parents[$term3->tid]), 'Both parents found successfully.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
