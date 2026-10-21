# TaxonomyLegacyTestCase::testTaxonomyLegacyNode()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 512–524 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L512-L524)
- **Class:** [TaxonomyLegacyTestCase](../TaxonomyLegacyTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyLegacyNode()
```

## Documentation

```text
Test taxonomy functionality with nodes prior to 1970.
```

## Code

```php
  function testTaxonomyLegacyNode() {
    // Posts an article with a taxonomy term and a date prior to 1970.
    $langcode = LANGUAGE_NONE;
    $edit = array();
    $edit['title'] = $this->randomName();
    $edit['date'] = '1969-01-01 00:00:00 -0500';
    $edit["body[$langcode][0][value]"] = $this->randomName();
    $edit["field_tags[$langcode]"] = $this->randomName();
    $this->drupalPost('node/add/article', $edit, t('Save'));
    // Checks that the node has been saved.
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertEqual($node->created, strtotime($edit['date']), 'Legacy node was saved with the right date.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
