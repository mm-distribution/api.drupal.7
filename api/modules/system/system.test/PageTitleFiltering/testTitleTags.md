# PageTitleFiltering::testTitleTags()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1623–1646 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1623-L1646)
- **Class:** [PageTitleFiltering](../PageTitleFiltering.md)
- **Module/theme:** system

## Signature

```php
function testTitleTags()
```

## Documentation

```text
Tests the handling of HTML by drupal_set_title() and drupal_get_title()
```

## Code

```php
  function testTitleTags() {
    $title = "string with <em>HTML</em>";
    // drupal_set_title's $filter is CHECK_PLAIN by default, so the title should be
    // returned with check_plain().
    drupal_set_title($title, CHECK_PLAIN);
    $this->assertTrue(strpos(drupal_get_title(), '<em>') === FALSE, 'Tags in title converted to entities when $output is CHECK_PLAIN.');
    // drupal_set_title's $filter is passed as PASS_THROUGH, so the title should be
    // returned with HTML.
    drupal_set_title($title, PASS_THROUGH);
    $this->assertTrue(strpos(drupal_get_title(), '<em>') !== FALSE, 'Tags in title are not converted to entities when $output is PASS_THROUGH.');
    // Generate node content.
    $langcode = LANGUAGE_NONE;
    $edit = array(
      "title" => '!SimpleTest! ' . $title . $this->randomName(20),
      "body[$langcode][0][value]" => '!SimpleTest! test body' . $this->randomName(200),
    );
    // Create the node with HTML in the title.
    $this->drupalPost('node/add/page', $edit, t('Save'));

    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->assertNotNull($node, 'Node created and found in database');
    $this->drupalGet("node/" . $node->nid);
    $this->assertText(check_plain($edit["title"]), 'Check to make sure tags in the node title are converted.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
