# TaxonomyRSSTestCase::testTaxonomyRSS()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1132–1167 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1132-L1167)
- **Class:** [TaxonomyRSSTestCase](../TaxonomyRSSTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyRSS()
```

## Documentation

```text
Tests that terms added to nodes are displayed in core RSS feed.

Create a node and assert that taxonomy terms appear in rss.xml.
```

## Code

```php
  function testTaxonomyRSS() {
    // Create two taxonomy terms.
    $term1 = $this->createTerm($this->vocabulary);

    // RSS display must be added manually.
    $this->drupalGet("admin/structure/types/manage/article/display");
    $edit = array(
      "view_modes_custom[rss]" => '1',
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    // Change the format to 'RSS category'.
    $this->drupalGet("admin/structure/types/manage/article/display/rss");
    $edit = array(
      "fields[taxonomy_" . $this->vocabulary->machine_name . "][type]" => 'taxonomy_term_reference_rss_category',
    );
    $this->drupalPost(NULL, $edit, t('Save'));

    // Post an article.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName();
    $edit[$this->instance['field_name'] . '[' . $langcode . '][]'] = $term1->tid;
    $this->drupalPost('node/add/article', $edit, t('Save'));

    // Check that the term is displayed when the RSS feed is viewed.
    $this->drupalGet('rss.xml');
    $test_element = array(
      'key' => 'category',
      'value' => $term1->name,
      'attributes' => array(
        'domain' => url('taxonomy/term/' . $term1->tid, array('absolute' => TRUE)),
      ),
    );
    $this->assertRaw(format_xml_elements(array($test_element)), 'Term is displayed when viewing the rss feed.');
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
