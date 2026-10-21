# TaxonomyHooksTestCase::testTaxonomyTermHooks()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1490–1524 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1490-L1524)
- **Class:** [TaxonomyHooksTestCase](../TaxonomyHooksTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermHooks()
```

## Documentation

```text
Test that hooks are run correctly on creating, editing, viewing,
and deleting a term.

@see taxonomy_test.module
```

## Code

```php
  function testTaxonomyTermHooks() {
    $vocabulary = $this->createVocabulary();

    // Create a term with one antonym.
    $edit = array(
      'name' => $this->randomName(),
      'antonym' => 'Long',
    );
    $this->drupalPost('admin/structure/taxonomy/' . $vocabulary->machine_name . '/add', $edit, t('Save'));
    $terms = taxonomy_get_term_by_name($edit['name']);
    $term = reset($terms);
    $this->assertEqual($term->antonym, $edit['antonym'], 'Antonym was loaded into the term object.');

    // Update the term with a different antonym.
    $edit = array(
      'name' => $this->randomName(),
      'antonym' => 'Short',
    );
    $this->drupalPost('taxonomy/term/' . $term->tid . '/edit', $edit, t('Save'));
    taxonomy_terms_static_reset();
    $term = taxonomy_term_load($term->tid);
    $this->assertEqual($edit['antonym'], $term->antonym, 'Antonym was successfully edited.');

    // View the term and ensure that hook_taxonomy_term_view() and
    // hook_entity_view() are invoked.
    $term = taxonomy_term_load($term->tid);
    $term_build = taxonomy_term_page($term);
    $this->assertFalse(empty($term_build['term_heading']['term']['taxonomy_test_term_view_check']), 'hook_taxonomy_term_view() was invoked when viewing the term.');
    $this->assertFalse(empty($term_build['term_heading']['term']['taxonomy_test_entity_view_check']), 'hook_entity_view() was invoked when viewing the term.');

    // Delete the term.
    taxonomy_term_delete($term->tid);
    $antonym = db_query('SELECT tid FROM {taxonomy_term_antonym} WHERE tid = :tid', array(':tid' => $term->tid))->fetchField();
    $this->assertFalse($antonym, 'The antonym were deleted from the database.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
