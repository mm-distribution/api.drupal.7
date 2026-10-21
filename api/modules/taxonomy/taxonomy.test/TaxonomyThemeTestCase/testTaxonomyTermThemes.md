# TaxonomyThemeTestCase::testTaxonomyTermThemes()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2035–2050 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2035-L2050)
- **Class:** [TaxonomyThemeTestCase](../TaxonomyThemeTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermThemes()
```

## Documentation

```text
Test the theme used when adding, viewing and editing taxonomy terms.
```

## Code

```php
  function testTaxonomyTermThemes() {
    // Adding a term to a vocabulary is considered an administrative action and
    // should use the administrative theme.
    $vocabulary = $this->createVocabulary();
    $this->drupalGet('admin/structure/taxonomy/' . $vocabulary->machine_name . '/add');
    $this->assertRaw('seven/style.css', "The administrative theme's CSS appears on the page for adding a taxonomy term.");

    // Viewing a taxonomy term should use the default theme.
    $term = $this->createTerm($vocabulary);
    $this->drupalGet('taxonomy/term/' . $term->tid);
    $this->assertRaw('bartik/css/style.css', "The default theme's CSS appears on the page for viewing a taxonomy term.");

    // Editing a taxonomy term should use the same theme as adding one.
    $this->drupalGet('taxonomy/term/' . $term->tid . '/edit');
    $this->assertRaw('seven/style.css', "The administrative theme's CSS appears on the page for editing a taxonomy term.");
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
