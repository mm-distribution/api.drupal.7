# TaxonomyTermTestCase::testTaxonomyGetTermByName()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 968–1022 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L968-L1022)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyGetTermByName()
```

## Documentation

```text
Test taxonomy_get_term_by_name().
```

## Code

```php
  function testTaxonomyGetTermByName() {
    $term = $this->createTerm($this->vocabulary);

    // Load the term with the exact name.
    $terms = taxonomy_get_term_by_name($term->name);
    $this->assertTrue(isset($terms[$term->tid]), 'Term loaded using exact name.');

    // Load the term with space concatenated.
    $terms  = taxonomy_get_term_by_name('  ' . $term->name . '   ');
    $this->assertTrue(isset($terms[$term->tid]), 'Term loaded with extra whitespace.');

    // Load the term with name uppercased.
    $terms = taxonomy_get_term_by_name(strtoupper($term->name));
    $this->assertTrue(isset($terms[$term->tid]), 'Term loaded with uppercased name.');

    // Load the term with name lowercased.
    $terms = taxonomy_get_term_by_name(strtolower($term->name));
    $this->assertTrue(isset($terms[$term->tid]), 'Term loaded with lowercased name.');

    // Try to load an invalid term name.
    $terms = taxonomy_get_term_by_name('Banana');
    $this->assertFalse($terms);

    // Try to load the term using a substring of the name.
    $terms = taxonomy_get_term_by_name(drupal_substr($term->name, 2));
    $this->assertFalse($terms);

    // Create a new term in a different vocabulary with the same name.
    $new_vocabulary = $this->createVocabulary();
    $new_term = new stdClass();
    $new_term->name = $term->name;
    $new_term->vid = $new_vocabulary->vid;
    taxonomy_term_save($new_term);

    // Load multiple terms with the same name.
    $terms = taxonomy_get_term_by_name($term->name);
    $this->assertEqual(count($terms), 2, 'Two terms loaded with the same name.');

    // Load single term when restricted to one vocabulary.
    $terms = taxonomy_get_term_by_name($term->name, $this->vocabulary->machine_name);
    $this->assertEqual(count($terms), 1, 'One term loaded when restricted by vocabulary.');
    $this->assertTrue(isset($terms[$term->tid]), 'Term loaded using exact name and vocabulary machine name.');

    // Create a new term with another name.
    $term2 = $this->createTerm($this->vocabulary);

    // Try to load a term by name that doesn't exist in this vocabulary but
    // exists in another vocabulary.
    $terms = taxonomy_get_term_by_name($term2->name, $new_vocabulary->machine_name);
    $this->assertFalse($terms, 'Invalid term name restricted by vocabulary machine name not loaded.');

    // Try to load terms filtering by a non-existing vocabulary.
    $terms = taxonomy_get_term_by_name($term2->name, 'non_existing_vocabulary');
    $this->assertEqual(count($terms), 0, 'No terms loaded when restricted by a non-existing vocabulary.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
