# TaxonomyTermFunctionTestCase::testTaxonomyVocabularyTree()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 437–485 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L437-L485)
- **Class:** [TaxonomyTermFunctionTestCase](../TaxonomyTermFunctionTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyVocabularyTree()
```

## Documentation

```text
Test a taxonomy with terms that have multiple parents of different depths.
```

## Code

```php
  function testTaxonomyVocabularyTree() {
    // Create a new vocabulary with 6 terms.
    $vocabulary = $this->createVocabulary();
    $term = array();
    for ($i = 0; $i < 6; $i++) {
      $term[$i] = $this->createTerm($vocabulary);
    }

    // $term[2] is a child of 1 and 5.
    $term[2]->parent = array($term[1]->tid, $term[5]->tid);
    taxonomy_term_save($term[2]);
    // $term[3] is a child of 2.
    $term[3]->parent = array($term[2]->tid);
    taxonomy_term_save($term[3]);
    // $term[5] is a child of 4.
    $term[5]->parent = array($term[4]->tid);
    taxonomy_term_save($term[5]);

    /**
     * Expected tree:
     * term[0] | depth: 0
     * term[1] | depth: 0
     * -- term[2] | depth: 1
     * ---- term[3] | depth: 2
     * term[4] | depth: 0
     * -- term[5] | depth: 1
     * ---- term[2] | depth: 2
     * ------ term[3] | depth: 3
     */
    // Count $term[1] parents with $max_depth = 1.
    $tree = taxonomy_get_tree($vocabulary->vid, $term[1]->tid, 1);
    $this->assertEqual(1, count($tree), 'We have one parent with depth 1.');

    // Count all vocabulary tree elements.
    $tree = taxonomy_get_tree($vocabulary->vid);
    $this->assertEqual(8, count($tree), 'We have all vocabulary tree elements.');

    // Count elements in every tree depth.
    foreach ($tree as $element) {
      if (!isset($depth_count[$element->depth])) {
        $depth_count[$element->depth] = 0;
      }
      $depth_count[$element->depth]++;
    }
    $this->assertEqual(3, $depth_count[0], 'Three elements in taxonomy tree depth 0.');
    $this->assertEqual(2, $depth_count[1], 'Two elements in taxonomy tree depth 1.');
    $this->assertEqual(2, $depth_count[2], 'Two elements in taxonomy tree depth 2.');
    $this->assertEqual(1, $depth_count[3], 'One element in taxonomy tree depth 3.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
