# TaxonomyTermTestCase::testTermMultipleParentsInterface()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 939–963 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L939-L963)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTermMultipleParentsInterface()
```

## Documentation

```text
Test saving a term with multiple parents through the UI.
```

## Code

```php
  function testTermMultipleParentsInterface() {
    // Add a new term to the vocabulary so that we can have multiple parents.
    $parent = $this->createTerm($this->vocabulary);

    // Add a new term with multiple parents.
    $edit = array(
      'name' => $this->randomName(12),
      'description[value]' => $this->randomName(100),
      'parent[]' => array(0, $parent->tid),
    );
    // Save the new term.
    $this->drupalPost('admin/structure/taxonomy/' . $this->vocabulary->machine_name . '/add', $edit, t('Save'));

    // Check that the term was successfully created.
    $terms = taxonomy_get_term_by_name($edit['name']);
    $term = reset($terms);
    $this->assertNotNull($term, 'Term found in database.');
    $this->assertEqual($edit['name'], $term->name, 'Term name was successfully saved.');
    $this->assertEqual($edit['description[value]'], $term->description, 'Term description was successfully saved.');
    // Check that the parent tid is still there. The other parent (<root>) is
    // not added by taxonomy_get_parents().
    $parents = taxonomy_get_parents($term->tid);
    $parent = reset($parents);
    $this->assertEqual($edit['parent[]'][1], $parent->tid, 'Term parents were successfully saved.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
