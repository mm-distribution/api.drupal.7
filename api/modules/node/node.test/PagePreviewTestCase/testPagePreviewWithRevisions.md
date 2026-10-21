# PagePreviewTestCase::testPagePreviewWithRevisions()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 564–594 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L564-L594)
- **Class:** [PagePreviewTestCase](../PagePreviewTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPagePreviewWithRevisions()
```

## Documentation

```text
Checks the node preview functionality, when using revisions.
```

## Code

```php
  function testPagePreviewWithRevisions() {
    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $body_key = "body[$langcode][0][value]";
    $term_key = "{$this->field_name}[$langcode]";
    // Force revision on "Basic page" content.
    variable_set('node_options_page', array('status', 'revision'));

    // Fill in node creation form and preview node.
    $edit = array();
    $edit[$title_key] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    $edit[$term_key] = $this->term->tid;
    $edit['log'] = $this->randomName(32);
    $this->drupalPost('node/add/page', $edit, t('Preview'));

    // Check that the preview is displaying the title, body, and term.
    $this->assertTitle(t('Preview | Drupal'), 'Basic page title is preview.');
    $this->assertText($edit[$title_key], 'Title displayed.');
    $this->assertText($edit[$body_key], 'Body displayed.');
    $this->assertText($this->term->name, 'Term displayed.');

    // Check that the title, body, and term fields are displayed with the
    // correct values.
    $this->assertFieldByName($title_key, $edit[$title_key], 'Title field displayed.');
    $this->assertFieldByName($body_key, $edit[$body_key], 'Body field displayed.');
    $this->assertFieldByName($term_key, $edit[$term_key], 'Term field displayed.');

    // Check that the log field has the correct value.
    $this->assertFieldByName('log', $edit['log'], 'Log field displayed.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
