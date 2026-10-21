# TaxonomyTermTestCase::testTermReorder()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 880–934 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L880-L934)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTermReorder()
```

## Documentation

```text
Save, edit and delete a term using the user interface.
```

## Code

```php
  function testTermReorder() {
    $this->createTerm($this->vocabulary);
    $this->createTerm($this->vocabulary);
    $this->createTerm($this->vocabulary);

    // Fetch the created terms in the default alphabetical order, i.e. term1
    // precedes term2 alphabetically, and term2 precedes term3.
    drupal_static_reset('taxonomy_get_tree');
    drupal_static_reset('taxonomy_get_treeparent');
    drupal_static_reset('taxonomy_get_treeterms');
    list($term1, $term2, $term3) = taxonomy_get_tree($this->vocabulary->vid);

    $this->drupalGet('admin/structure/taxonomy/' . $this->vocabulary->machine_name);

    // Each term has four hidden fields, "tid:1:0[tid]", "tid:1:0[parent]",
    // "tid:1:0[depth]", and "tid:1:0[weight]". Change the order to term2,
    // term3, term1 by setting weight property, make term3 a child of term2 by
    // setting the parent and depth properties, and update all hidden fields.
    $edit = array(
      'tid:' . $term2->tid . ':0[tid]' => $term2->tid,
      'tid:' . $term2->tid . ':0[parent]' => 0,
      'tid:' . $term2->tid . ':0[depth]' => 0,
      'tid:' . $term2->tid . ':0[weight]' => 0,
      'tid:' . $term3->tid . ':0[tid]' => $term3->tid,
      'tid:' . $term3->tid . ':0[parent]' => $term2->tid,
      'tid:' . $term3->tid . ':0[depth]' => 1,
      'tid:' . $term3->tid . ':0[weight]' => 1,
      'tid:' . $term1->tid . ':0[tid]' => $term1->tid,
      'tid:' . $term1->tid . ':0[parent]' => 0,
      'tid:' . $term1->tid . ':0[depth]' => 0,
      'tid:' . $term1->tid . ':0[weight]' => 2,
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    drupal_static_reset('taxonomy_get_tree');
    drupal_static_reset('taxonomy_get_treeparent');
    drupal_static_reset('taxonomy_get_treeterms');
    $terms = taxonomy_get_tree($this->vocabulary->vid);
    $this->assertEqual($terms[0]->tid, $term2->tid, 'Term 2 was moved above term 1.');
    $this->assertEqual($terms[1]->parents, array($term2->tid), 'Term 3 was made a child of term 2.');
    $this->assertEqual($terms[2]->tid, $term1->tid, 'Term 1 was moved below term 2.');

    $this->drupalPost('admin/structure/taxonomy/' . $this->vocabulary->machine_name, array(), t('Reset to alphabetical'));
    // Submit confirmation form.
    $this->drupalPost(NULL, array(), t('Reset to alphabetical'));

    drupal_static_reset('taxonomy_get_tree');
    drupal_static_reset('taxonomy_get_treeparent');
    drupal_static_reset('taxonomy_get_treeterms');
    $terms = taxonomy_get_tree($this->vocabulary->vid);
    $this->assertEqual($terms[0]->tid, $term1->tid, 'Term 1 was moved to back above term 2.');
    $this->assertEqual($terms[1]->tid, $term2->tid, 'Term 2 was moved to back below term 1.');
    $this->assertEqual($terms[2]->tid, $term3->tid, 'Term 3 is still below term 2.');
    $this->assertEqual($terms[2]->parents, array($term2->tid), 'Term 3 is still a child of term 2.' . var_export($terms[1]->tid, 1));
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
