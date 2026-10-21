# TaxonomyTermIndexTestCase::testTaxonomyIndex()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1266–1378 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1266-L1378)
- **Class:** [TaxonomyTermIndexTestCase](../TaxonomyTermIndexTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyIndex()
```

## Documentation

```text
Tests that the taxonomy index is maintained properly.
```

## Code

```php
  function testTaxonomyIndex() {
    // Create terms in the vocabulary.
    $term_1 = $this->createTerm($this->vocabulary);
    $term_2 = $this->createTerm($this->vocabulary);

    // Post an article.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $edit["{$this->field_name_1}[$langcode][]"] = $term_1->tid;
    $edit["{$this->field_name_2}[$langcode][]"] = $term_1->tid;
    $this->drupalPost('node/add/article', $edit, t('Save'));

    // Check that the term is indexed, and only once.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 1 is indexed once.');

    // Update the article to change one term.
    $edit["{$this->field_name_1}[$langcode][]"] = $term_2->tid;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    // Check that both terms are indexed.
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 1 is indexed.');
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_2->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 2 is indexed.');

    // Update the article to change another term.
    $edit["{$this->field_name_2}[$langcode][]"] = $term_2->tid;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    // Check that only one term is indexed.
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(0, $index_count, 'Term 1 is not indexed.');
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_2->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 2 is indexed once.');

    // Redo the above tests without interface.
    $update_node = array(
      'nid' => $node->nid,
      'vid' => $node->vid,
      'uid' => $node->uid,
      'type' => $node->type,
      'title' => $this->randomName(),
    );

    // Update the article with no term changed.
    $updated_node = (object) $update_node;
    node_save($updated_node);

    // Check that the index was not changed.
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(0, $index_count, 'Term 1 is not indexed.');
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_2->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 2 is indexed once.');

    // Update the article to change one term.
    $update_node[$this->field_name_1][$langcode] = array(array('tid' => $term_1->tid));
    $updated_node = (object) $update_node;
    node_save($updated_node);

    // Check that both terms are indexed.
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 1 is indexed.');
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_2->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 2 is indexed.');

    // Update the article to change another term.
    $update_node[$this->field_name_2][$langcode] = array(array('tid' => $term_1->tid));
    $updated_node = (object) $update_node;
    node_save($updated_node);

    // Check that only one term is indexed.
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_1->tid,
    ))->fetchField();
    $this->assertEqual(1, $index_count, 'Term 1 is indexed once.');
    $index_count = db_query('SELECT COUNT(*) FROM {taxonomy_index} WHERE nid = :nid AND tid = :tid', array(
      ':nid' => $node->nid,
      ':tid' => $term_2->tid,
    ))->fetchField();
    $this->assertEqual(0, $index_count, 'Term 2 is not indexed.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
