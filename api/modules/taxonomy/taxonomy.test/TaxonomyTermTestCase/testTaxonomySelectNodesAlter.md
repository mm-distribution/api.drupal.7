# TaxonomyTermTestCase::testTaxonomySelectNodesAlter()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1028–1045 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1028-L1045)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
public function testTaxonomySelectNodesAlter()
```

## Documentation

```text
Tests that taxonomy term detail page is working even after the default
taxonomy_select_nodes() query is altered.
```

## Code

```php
  public function testTaxonomySelectNodesAlter() {
    // Create a new term.
    $term = $this->createTerm($this->vocabulary);

    // Create an article.
    $settings = array(
      'type' => 'article',
      $this->instance['field_name'] => array(LANGUAGE_NONE => array(array('tid' => $term->tid))),
    );
    $this->drupalCreateNode($settings);

    // Check if the taxonomy term detail page is working.
    module_enable(array('taxonomy_nodes_test'));
    variable_set('taxonomy_nodes_test_query_node_access_alter', TRUE);
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $this->assertResponse(200, 'The taxonomy term page is working.');
    variable_set('taxonomy_nodes_test_query_node_access_alter', FALSE);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
