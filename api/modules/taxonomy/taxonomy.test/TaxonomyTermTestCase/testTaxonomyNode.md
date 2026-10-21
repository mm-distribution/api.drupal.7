# TaxonomyTermTestCase::testTaxonomyNode()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 623–653 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L623-L653)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyNode()
```

## Documentation

```text
Test that hook_node_$op implementations work correctly.

Save & edit a node and assert that taxonomy terms are saved/loaded properly.
```

## Code

```php
  function testTaxonomyNode() {
    // Create two taxonomy terms.
    $term1 = $this->createTerm($this->vocabulary);
    $term2 = $this->createTerm($this->vocabulary);

    // Post an article.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $edit[$this->instance['field_name'] . '[' . $langcode . '][]'] = $term1->tid;
    $this->drupalPost('node/add/article', $edit, t('Save'));

    // Check that the term is displayed when the node is viewed.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($term1->name, 'Term is displayed when viewing the node.');

    // Edit the node with a different term.
    $edit[$this->instance['field_name'] . '[' . $langcode . '][]'] = $term2->tid;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    $this->drupalGet('node/' . $node->nid);
    $this->assertText($term2->name, 'Term is displayed when viewing the node.');

    // Preview the node.
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Preview'));
    $this->assertNoUniqueText($term2->name, 'Term is displayed when previewing the node.');
    $this->drupalPost(NULL, NULL, t('Preview'));
    $this->assertNoUniqueText($term2->name, 'Term is displayed when previewing the node again.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
