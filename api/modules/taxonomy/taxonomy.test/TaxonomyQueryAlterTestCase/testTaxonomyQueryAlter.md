# TaxonomyQueryAlterTestCase::testTaxonomyQueryAlter()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2130–2193 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2130-L2193)
- **Class:** [TaxonomyQueryAlterTestCase](../TaxonomyQueryAlterTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
public function testTaxonomyQueryAlter()
```

## Documentation

```text
Tests that appropriate tags are added when querying the database.
```

## Code

```php
  public function testTaxonomyQueryAlter() {
    // Create a new vocabulary and add a few terms to it.
    $vocabulary = $this->createVocabulary();
    $terms = array();
    for ($i = 0; $i < 5; $i++) {
      $terms[$i] = $this->createTerm($vocabulary);
    }

    // Set up hierarchy. Term 2 is a child of 1.
    $terms[2]->parent = array($terms[1]->tid);
    taxonomy_term_save($terms[2]);

    $this->setupQueryTagTestHooks();
    $loaded_term = taxonomy_term_load($terms[0]->tid);
    $this->assertEqual($loaded_term->tid, $terms[0]->tid, 'First term was loaded');
    $this->assertQueryTagTestResult(1, 'taxonomy_term_load()');

    $this->setupQueryTagTestHooks();
    $loaded_terms = taxonomy_get_tree($vocabulary->vid);
    $this->assertEqual(count($loaded_terms), count($terms), 'All terms were loaded');
    $this->assertQueryTagTestResult(1, 'taxonomy_get_tree()');

    $this->setupQueryTagTestHooks();
    $loaded_terms = taxonomy_get_parents($terms[2]->tid);
    $this->assertEqual(count($loaded_terms), 1, 'All parent terms were loaded');
    $this->assertQueryTagTestResult(2, 'taxonomy_get_parents()');

    $this->setupQueryTagTestHooks();
    $loaded_terms = taxonomy_get_children($terms[1]->tid);
    $this->assertEqual(count($loaded_terms), 1, 'All child terms were loaded');
    $this->assertQueryTagTestResult(2, 'taxonomy_get_children()');

    $this->setupQueryTagTestHooks();
    $query = db_select('taxonomy_term_data', 't');
    $query->addField('t', 'tid');
    $query->addTag('taxonomy_term_access');
    $tids = $query->execute()->fetchCol();
    $this->assertEqual(count($tids), count($terms), 'All term IDs were retrieved');
    $this->assertQueryTagTestResult(1, 'custom db_select() with taxonomy_term_access tag (preferred)');

    $this->setupQueryTagTestHooks();
    $query = db_select('taxonomy_term_data', 't');
    $query->addField('t', 'tid');
    $query->addTag('term_access');
    $tids = $query->execute()->fetchCol();
    $this->assertEqual(count($tids), count($terms), 'All term IDs were retrieved');
    $this->assertQueryTagTestResult(1, 'custom db_select() with term_access tag (deprecated)');

    $this->setupQueryTagTestHooks();
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'taxonomy_term');
    $query->addTag('taxonomy_term_access');
    $result = $query->execute();
    $this->assertEqual(count($result['taxonomy_term']), count($terms), 'All term IDs were retrieved');
    $this->assertQueryTagTestResult(1, 'custom EntityFieldQuery with taxonomy_term_access tag (preferred)');

    $this->setupQueryTagTestHooks();
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'taxonomy_term');
    $query->addTag('term_access');
    $result = $query->execute();
    $this->assertEqual(count($result['taxonomy_term']), count($terms), 'All term IDs were retrieved');
    $this->assertQueryTagTestResult(1, 'custom EntityFieldQuery with term_access tag (deprecated)');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
