# TaxonomyPrivateFileTestCase::testTaxonomyImageAccess()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2306–2331 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2306-L2331)
- **Class:** [TaxonomyPrivateFileTestCase](../TaxonomyPrivateFileTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
public function testTaxonomyImageAccess()
```

## Documentation

```text
Tests access to a private file on a taxonomy term entity.
```

## Code

```php
  public function testTaxonomyImageAccess() {
    $user = $this->drupalCreateUser(array('administer site configuration', 'administer taxonomy', 'access user profiles'));
    $this->drupalLogin($user);

    // Create a term and upload the image.
    $term = $this->createTerm($this->vocabulary);
    $files = $this->drupalGetTestFiles('image');
    $image = array_pop($files);
    $edit['files[field_test_' . LANGUAGE_NONE . '_0]'] = drupal_realpath($image->uri);
    $this->drupalPost('taxonomy/term/' . $term->tid . '/edit', $edit, t('Save'));
    $term = taxonomy_term_load($term->tid);
    $this->assertText(t('Updated term @name.', array('@name' => $term->name)));

    // Create a user that should have access to the file and one that doesn't.
    $access_user = $this->drupalCreateUser(array('access content'));
    $no_access_user = $this->drupalCreateUser();
    $image = file_load($term->field_test[LANGUAGE_NONE][0]['fid']);
    $image_url = file_create_url($image->uri);
    $this->drupalLogin($access_user);
    $this->drupalGet($image_url);
    $this->assertResponse(200, 'Private image on term is accessible with right permission');

    $this->drupalLogin($no_access_user);
    $this->drupalGet($image_url);
    $this->assertResponse(403, 'Private image on term not accessible without right permission');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
