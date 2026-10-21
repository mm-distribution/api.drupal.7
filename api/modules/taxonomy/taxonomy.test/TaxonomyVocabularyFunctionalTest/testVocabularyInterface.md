# TaxonomyVocabularyFunctionalTest::testVocabularyInterface()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 70–115 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L70-L115)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
- **Module/theme:** taxonomy

## Signature

```php
function testVocabularyInterface()
```

## Documentation

```text
Create, edit and delete a vocabulary via the user interface.
```

## Code

```php
  function testVocabularyInterface() {
    // Visit the main taxonomy administration page.
    $this->drupalGet('admin/structure/taxonomy');

    // Create a new vocabulary.
    $this->clickLink(t('Add vocabulary'));
    $edit = array();
    $machine_name = drupal_strtolower($this->randomName());
    $edit['name'] = $this->randomName();
    $edit['description'] = $this->randomName();
    $edit['machine_name'] = $machine_name;
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->assertRaw(t('Created new vocabulary %name.', array('%name' => $edit['name'])), 'Vocabulary created successfully.');

    // Edit the vocabulary.
    $this->drupalGet('admin/structure/taxonomy');
    $this->assertText($edit['name'], 'Vocabulary found in the vocabulary overview listing.');
    $this->clickLink(t('edit vocabulary'));
    $edit = array();
    $edit['name'] = $this->randomName();
    $this->drupalPost(NULL, $edit, t('Save'));
    $this->drupalGet('admin/structure/taxonomy');
    $this->assertText($edit['name'], 'Vocabulary found in the vocabulary overview listing.');

    // Try to submit a vocabulary with a duplicate machine name.
    $edit['machine_name'] = $machine_name;
    $this->drupalPost('admin/structure/taxonomy/add', $edit, t('Save'));
    $this->assertText(t('The machine-readable name is already in use. It must be unique.'));

    // Try to submit an invalid machine name.
    $edit['machine_name'] = '!&^%';
    $this->drupalPost('admin/structure/taxonomy/add', $edit, t('Save'));
    $this->assertText(t('The machine-readable name must contain only lowercase letters, numbers, and underscores.'));

    // Ensure that vocabulary titles are escaped properly.
    $edit = array();
    $edit['name'] = 'Don\'t Panic';
    $edit['description'] = $this->randomName();
    $edit['machine_name'] = 'don_t_panic';
    $this->drupalPost('admin/structure/taxonomy/add', $edit, t('Save'));

    $site_name = variable_get('site_name', 'Drupal');
    $this->drupalGet('admin/structure/taxonomy/don_t_panic');
    $this->assertTitle(t('Don\'t Panic | @site-name', array('@site-name' => $site_name)));
    $this->assertNoTitle(t('Don&#039;t Panic | @site-name', array('@site-name' => $site_name)));
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
