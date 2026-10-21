# TaxonomyTermTestCase::testTermInterface()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 808–875 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L808-L875)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTermInterface()
```

## Documentation

```text
Save, edit and delete a term using the user interface.
```

## Code

```php
  function testTermInterface() {
    $edit = array(
      'name' => $this->randomName(12),
      'description[value]' => $this->randomName(100),
    );
    // Explicitly set the parents field to 'root', to ensure that
    // taxonomy_form_term_submit() handles the invalid term ID correctly.
    $edit['parent[]'] = array(0);

    // Create the term to edit.
    $this->drupalPost('admin/structure/taxonomy/' . $this->vocabulary->machine_name . '/add', $edit, t('Save'));

    $terms = taxonomy_get_term_by_name($edit['name']);
    $term = reset($terms);
    $this->assertNotNull($term, 'Term found in database.');

    // Submitting a term takes us to the add page; we need the List page.
    $this->drupalGet('admin/structure/taxonomy/' . $this->vocabulary->machine_name);

    // Test edit link as accessed from Taxonomy administration pages.
    // Because Simpletest creates its own database when running tests, we know
    // the first edit link found on the listing page is to our term.
    $this->clickLink(t('edit'));

    $this->assertRaw($edit['name'], 'The randomly generated term name is present.');
    $this->assertText($edit['description[value]'], 'The randomly generated term description is present.');

    $edit = array(
      'name' => $this->randomName(14),
      'description[value]' => $this->randomName(102),
    );

    // Edit the term.
    $this->drupalPost('taxonomy/term/' . $term->tid . '/edit', $edit, t('Save'));

    // Check that the term is still present at admin UI after edit.
    $this->drupalGet('admin/structure/taxonomy/' . $this->vocabulary->machine_name);
    $this->assertText($edit['name'], 'The randomly generated term name is present.');
    $this->assertLink(t('edit'));

    // View the term and check that it is correct.
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $this->assertText($edit['name'], 'The randomly generated term name is present.');
    $this->assertText($edit['description[value]'], 'The randomly generated term description is present.');

    // Did this page request display a 'term-listing-heading'?
    $this->assertPattern('|class="taxonomy-term-description"|', 'Term page displayed the term description element.');
    // Check that it does NOT show a description when description is blank.
    $term->description = '';
    taxonomy_term_save($term);
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $this->assertNoPattern('|class="taxonomy-term-description"|', 'Term page did not display the term description when description was blank.');

    // Check that the term feed page is working.
    $this->drupalGet('taxonomy/term/' . $term->tid . '/feed');

    // Check that the term edit page does not try to interpret additional path
    // components as arguments for taxonomy_form_term().
    $this->drupalGet('taxonomy/term/' . $term->tid . '/edit/' . $this->randomName());

    // Delete the term.
    $this->drupalPost('taxonomy/term/' . $term->tid . '/edit', array(), t('Delete'));
    $this->drupalPost(NULL, NULL, t('Delete'));

    // Assert that the term no longer exists.
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $this->assertResponse(404, 'The taxonomy term page was not found.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
