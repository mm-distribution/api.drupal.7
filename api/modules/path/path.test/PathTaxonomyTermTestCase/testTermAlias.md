# PathTaxonomyTermTestCase::testTermAlias()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 296–334 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L296-L334)
- **Class:** [PathTaxonomyTermTestCase](../PathTaxonomyTermTestCase.md)
- **Module/theme:** path

## Signature

```php
function testTermAlias()
```

## Documentation

```text
Tests alias functionality through the admin interfaces.
```

## Code

```php
  function testTermAlias() {
    // Create a term in the default 'Tags' vocabulary with URL alias.
    $vocabulary = taxonomy_vocabulary_load(1);
    $description = $this->randomName();;
    $edit = array();
    $edit['name'] = $this->randomName();
    $edit['description[value]'] = $description;
    $edit['path[alias]'] = $this->randomName();
    $this->drupalPost('admin/structure/taxonomy/' . $vocabulary->machine_name . '/add', $edit, t('Save'));

    // Confirm that the alias works.
    $this->drupalGet($edit['path[alias]']);
    $this->assertText($description, 'Term can be accessed on URL alias.');

    // Change the term's URL alias.
    $tid = db_query("SELECT tid FROM {taxonomy_term_data} WHERE name = :name", array(':name' => $edit['name']))->fetchField();
    $edit2 = array();
    $edit2['path[alias]'] = $this->randomName();
    $this->drupalPost('taxonomy/term/' . $tid . '/edit', $edit2, t('Save'));

    // Confirm that the changed alias works.
    $this->drupalGet($edit2['path[alias]']);
    $this->assertText($description, 'Term can be accessed on changed URL alias.');

    // Confirm that the old alias no longer works.
    $this->drupalGet($edit['path[alias]']);
    $this->assertNoText($description, 'Old URL alias has been removed after altering.');
    $this->assertResponse(404, 'Old URL alias returns 404.');

    // Remove the term's URL alias.
    $edit3 = array();
    $edit3['path[alias]'] = '';
    $this->drupalPost('taxonomy/term/' . $tid . '/edit', $edit3, t('Save'));

    // Confirm that the alias no longer works.
    $this->drupalGet($edit2['path[alias]']);
    $this->assertNoText($description, 'Old URL alias has been removed after altering.');
    $this->assertResponse(404, 'Old URL alias returns 404.');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
